from __future__ import annotations

import csv
from datetime import date
from itertools import count
from pathlib import Path

from src.enums import Prioridade, Status
from src.models import Projeto, Tarefa, Usuario


class GerenciadorTarefas:
    """Coordena usuários, projetos, tarefas, relatórios e exportações."""

    def __init__(self) -> None:
        self.__usuarios: dict[int, Usuario] = {}
        self.__ids_usuarios = count(1)
        self.__ids_projetos = count(1)
        self.__ids_tarefas = count(1)

    @property
    def usuarios(self) -> tuple[Usuario, ...]:
        return tuple(self.__usuarios.values())

    def criar_usuario(self, nome: str, email: str, senha: str) -> Usuario:
        if any(usuario.email == email.strip().lower() for usuario in self.usuarios):
            raise ValueError("Já existe um usuário com esse e-mail.")
        usuario = Usuario(next(self.__ids_usuarios), nome, email, senha)
        self.__usuarios[usuario.id] = usuario
        return usuario

    def listar_usuarios(self) -> tuple[Usuario, ...]:
        return self.usuarios

    def buscar_usuario(self, identificador: int) -> Usuario:
        try:
            return self.__usuarios[identificador]
        except KeyError as erro:
            raise ValueError("Usuário não encontrado.") from erro

    def remover_usuario(self, identificador: int) -> Usuario:
        return self.__usuarios.pop(self.buscar_usuario(identificador).id)

    def criar_projeto(
        self,
        usuario_id: int,
        nome: str,
        descricao: str,
        data_criacao: date | None = None,
    ) -> Projeto:
        usuario = self.buscar_usuario(usuario_id)
        return usuario.criar_projeto(
            next(self.__ids_projetos), nome, descricao, data_criacao
        )

    def listar_projetos(self) -> tuple[Projeto, ...]:
        return tuple(
            projeto
            for usuario in self.usuarios
            for projeto in usuario.listar_projetos()
        )

    def buscar_projeto(self, identificador: int) -> Projeto:
        for projeto in self.listar_projetos():
            if projeto.id == identificador:
                return projeto
        raise ValueError("Projeto não encontrado.")

    def remover_projeto(self, identificador: int) -> Projeto:
        projeto = self.buscar_projeto(identificador)
        return projeto.usuario.remover_projeto(identificador)

    def criar_tarefa(
        self,
        projeto_id: int,
        titulo: str,
        descricao: str,
        prioridade: Prioridade,
        data_limite: date,
    ) -> Tarefa:
        projeto = self.buscar_projeto(projeto_id)
        return projeto.criar_tarefa(
            next(self.__ids_tarefas),
            titulo,
            descricao,
            prioridade,
            data_limite,
        )

    def listar_tarefas(self) -> tuple[Tarefa, ...]:
        return tuple(tarefa for projeto in self.listar_projetos() for tarefa in projeto.tarefas)

    def buscar_tarefa(self, identificador: int) -> Tarefa:
        for tarefa in self.listar_tarefas():
            if tarefa.id == identificador:
                return tarefa
        raise ValueError("Tarefa não encontrada.")

    def tarefas_pendentes_por_prioridade(self) -> dict[Prioridade, list[Tarefa]]:
        resultado: dict[Prioridade, list[Tarefa]] = {
            prioridade: [] for prioridade in reversed(list(Prioridade))
        }
        for tarefa in self.listar_tarefas():
            if tarefa.status != Status.CONCLUIDA:
                resultado[tarefa.prioridade].append(tarefa)
        return resultado

    def projetos_por_progresso(self) -> list[Projeto]:
        return sorted(
            self.listar_projetos(),
            key=lambda projeto: (-projeto.calcular_progresso(), projeto.nome.lower()),
        )

    def total_concluidas_por_usuario(self) -> dict[Usuario, int]:
        return {
            usuario: sum(
                tarefa.status == Status.CONCLUIDA
                for projeto in usuario.projetos
                for tarefa in projeto.tarefas
            )
            for usuario in self.usuarios
        }

    def gerar_relatorio_texto(self) -> str:
        linhas = ["RELATÓRIO DE PRODUTIVIDADE", "=" * 32]
        linhas.append("\nTAREFAS PENDENTES POR PRIORIDADE")
        for prioridade, tarefas in self.tarefas_pendentes_por_prioridade().items():
            linhas.append(f"- {prioridade}: {len(tarefas)}")
            linhas.extend(f"  • {tarefa.titulo} ({tarefa.projeto.nome})" for tarefa in tarefas)

        linhas.append("\nPROJETOS POR PERCENTUAL DE CONCLUSÃO")
        for projeto in self.projetos_por_progresso():
            linhas.append(f"- {projeto.nome}: {projeto.calcular_progresso():.1f}%")

        linhas.append("\nTAREFAS CONCLUÍDAS POR USUÁRIO")
        for usuario, total in self.total_concluidas_por_usuario().items():
            linhas.append(f"- {usuario.nome}: {total}")
        return "\n".join(linhas)

    def exportar_relatorio(self, destino: str | Path, formato: str = "txt") -> Path:
        caminho = Path(destino)
        formato_normalizado = formato.lower()
        if formato_normalizado not in {"txt", "csv"}:
            raise ValueError("O formato deve ser txt ou csv.")
        caminho.mkdir(parents=True, exist_ok=True)
        arquivo = caminho / f"relatorio_produtividade.{formato_normalizado}"

        if formato_normalizado == "txt":
            arquivo.write_text(self.gerar_relatorio_texto(), encoding="utf-8")
            return arquivo

        with arquivo.open("w", newline="", encoding="utf-8-sig") as stream:
            writer = csv.writer(stream, delimiter=";")
            writer.writerow(["tipo", "item", "valor"])
            for prioridade, tarefas in self.tarefas_pendentes_por_prioridade().items():
                writer.writerow(["tarefas pendentes", prioridade.name, len(tarefas)])
            for projeto in self.projetos_por_progresso():
                writer.writerow(["progresso", projeto.nome, f"{projeto.calcular_progresso():.1f}%"])
            for usuario, total in self.total_concluidas_por_usuario().items():
                writer.writerow(["concluídas", usuario.nome, total])
        return arquivo

