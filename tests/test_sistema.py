import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path

from src.enums import Prioridade, Status
from src.services import GerenciadorTarefas


class TestGerenciadorTarefas(unittest.TestCase):
    def setUp(self) -> None:
        self.sistema = GerenciadorTarefas()
        self.usuario = self.sistema.criar_usuario(
            "Kayky Moreira Assunção", "kayky@exemplo.com", "1234"
        )
        self.projeto = self.sistema.criar_projeto(
            self.usuario.id, "Projeto POO", "Projeto de teste"
        )

    def criar_tarefa(self, titulo: str, prioridade: Prioridade = Prioridade.MEDIA):
        return self.sistema.criar_tarefa(
            self.projeto.id,
            titulo,
            "Descrição de teste",
            prioridade,
            date.today() + timedelta(days=1),
        )

    def test_usuario_possui_projeto(self) -> None:
        self.assertEqual(self.usuario.projetos, (self.projeto,))
        self.assertIs(self.projeto.usuario, self.usuario)

    def test_projeto_calcula_progresso(self) -> None:
        primeira = self.criar_tarefa("Primeira")
        self.criar_tarefa("Segunda")
        primeira.marcar_concluida()
        self.assertEqual(self.projeto.calcular_progresso(), 50.0)

    def test_fluxo_de_status(self) -> None:
        tarefa = self.criar_tarefa("Implementar")
        self.assertEqual(tarefa.status, Status.PENDENTE)
        tarefa.iniciar()
        self.assertEqual(tarefa.status, Status.EM_ANDAMENTO)
        tarefa.marcar_concluida()
        self.assertEqual(tarefa.status, Status.CONCLUIDA)
        self.assertFalse(tarefa.esta_vencida(date.today() + timedelta(days=10)))

    def test_tarefa_vencida(self) -> None:
        projeto_antigo = self.sistema.criar_projeto(
            self.usuario.id,
            "Projeto antigo",
            "Teste de vencimento",
            date.today() - timedelta(days=10),
        )
        tarefa = self.sistema.criar_tarefa(
            projeto_antigo.id,
            "Tarefa atrasada",
            "Descrição",
            Prioridade.ALTA,
            date.today() - timedelta(days=1),
        )
        self.assertTrue(tarefa.esta_vencida())

    def test_relatorios_obrigatorios(self) -> None:
        concluida = self.criar_tarefa("Concluída", Prioridade.ALTA)
        self.criar_tarefa("Pendente", Prioridade.URGENTE)
        concluida.marcar_concluida()

        self.assertEqual(len(self.sistema.tarefas_pendentes_por_prioridade()[Prioridade.URGENTE]), 1)
        self.assertEqual(self.sistema.projetos_por_progresso()[0], self.projeto)
        self.assertEqual(self.sistema.total_concluidas_por_usuario()[self.usuario], 1)

    def test_exportacao_txt_e_csv(self) -> None:
        self.criar_tarefa("Exportar")
        with tempfile.TemporaryDirectory() as pasta:
            txt = self.sistema.exportar_relatorio(pasta, "txt")
            csv = self.sistema.exportar_relatorio(pasta, "csv")
            self.assertTrue(txt.exists())
            self.assertTrue(csv.exists())
            self.assertIn("RELATÓRIO DE PRODUTIVIDADE", txt.read_text(encoding="utf-8"))

    def test_impede_email_duplicado(self) -> None:
        with self.assertRaisesRegex(ValueError, "e-mail"):
            self.sistema.criar_usuario("Outra pessoa", "kayky@exemplo.com", "5678")

    def test_remove_projeto_e_usuario(self) -> None:
        removido = self.sistema.remover_projeto(self.projeto.id)
        self.assertEqual(removido, self.projeto)
        self.assertEqual(self.sistema.listar_projetos(), ())
        self.sistema.remover_usuario(self.usuario.id)
        self.assertEqual(self.sistema.listar_usuarios(), ())


if __name__ == "__main__":
    unittest.main()

