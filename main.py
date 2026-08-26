from __future__ import annotations

import argparse
from datetime import date, datetime, timedelta
from pathlib import Path

from src.enums import Prioridade
from src.services import GerenciadorTarefas


def ler_inteiro(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_data(mensagem: str) -> date:
    while True:
        try:
            return datetime.strptime(input(mensagem), "%d/%m/%Y").date()
        except ValueError:
            print("Informe a data no formato DD/MM/AAAA.")


def ler_prioridade() -> Prioridade:
    print("1 - Baixa | 2 - Média | 3 - Alta | 4 - Urgente")
    while True:
        try:
            return Prioridade(ler_inteiro("Prioridade: "))
        except ValueError:
            print("Escolha uma prioridade entre 1 e 4.")


def exibir_menu() -> None:
    print(
        "\n=== GERENCIADOR INTELIGENTE DE TAREFAS ===\n"
        "1 - Cadastrar usuário\n"
        "2 - Listar usuários\n"
        "3 - Criar projeto\n"
        "4 - Listar projetos\n"
        "5 - Criar tarefa\n"
        "6 - Listar tarefas\n"
        "7 - Alterar status de tarefa\n"
        "8 - Exibir relatórios\n"
        "9 - Exportar relatórios\n"
        "10 - Remover projeto\n"
        "11 - Remover usuário\n"
        "0 - Sair"
    )


def executar_menu() -> None:
    sistema = GerenciadorTarefas()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        try:
            if opcao == "0":
                print("Sistema encerrado.")
                break
            if opcao == "1":
                usuario = sistema.criar_usuario(
                    input("Nome: "), input("E-mail: "), input("Senha: ")
                )
                print(f"Usuário criado: {usuario}")
            elif opcao == "2":
                print("\n".join(map(str, sistema.listar_usuarios())) or "Nenhum usuário cadastrado.")
            elif opcao == "3":
                projeto = sistema.criar_projeto(
                    ler_inteiro("ID do usuário: "),
                    input("Nome do projeto: "),
                    input("Descrição: "),
                )
                print(f"Projeto criado: {projeto}")
            elif opcao == "4":
                print("\n".join(map(str, sistema.listar_projetos())) or "Nenhum projeto cadastrado.")
            elif opcao == "5":
                tarefa = sistema.criar_tarefa(
                    ler_inteiro("ID do projeto: "),
                    input("Título: "),
                    input("Descrição: "),
                    ler_prioridade(),
                    ler_data("Data limite (DD/MM/AAAA): "),
                )
                print(f"Tarefa criada: {tarefa}")
            elif opcao == "6":
                print("\n".join(map(str, sistema.listar_tarefas())) or "Nenhuma tarefa cadastrada.")
            elif opcao == "7":
                tarefa = sistema.buscar_tarefa(ler_inteiro("ID da tarefa: "))
                acao = input("1 - Iniciar | 2 - Concluir | 3 - Reabrir: ").strip()
                {"1": tarefa.iniciar, "2": tarefa.marcar_concluida, "3": tarefa.reabrir}[acao]()
                print(f"Status atualizado: {tarefa}")
            elif opcao == "8":
                print("\n" + sistema.gerar_relatorio_texto())
            elif opcao == "9":
                formato = input("Formato (txt/csv): ").strip().lower()
                arquivo = sistema.exportar_relatorio(Path(__file__).parent / "exports", formato)
                print(f"Relatório exportado para: {arquivo}")
            elif opcao == "10":
                print(f"Projeto removido: {sistema.remover_projeto(ler_inteiro('ID do projeto: ')).nome}")
            elif opcao == "11":
                print(f"Usuário removido: {sistema.remover_usuario(ler_inteiro('ID do usuário: ')).nome}")
            else:
                print("Opção inválida.")
        except (ValueError, KeyError) as erro:
            print(f"Não foi possível concluir: {erro}")


def executar_demonstracao() -> None:
    """Executa um cenário completo sem solicitar dados pelo teclado."""
    sistema = GerenciadorTarefas()
    usuario = sistema.criar_usuario(
        "Kayky Moreira Assunção", "kayky.moreira@exemplo.com", "poo2026"
    )
    projeto = sistema.criar_projeto(
        usuario.id,
        "Atividade de Programação Orientada a Objetos",
        "Organização e entrega do projeto inteligente.",
    )
    tarefa_modelagem = sistema.criar_tarefa(
        projeto.id,
        "Modelar as classes",
        "Criar Usuario, Projeto, Tarefa, Prioridade e Status.",
        Prioridade.URGENTE,
        date.today() + timedelta(days=1),
    )
    tarefa_codigo = sistema.criar_tarefa(
        projeto.id,
        "Implementar o sistema",
        "Programar regras, menu e relatórios.",
        Prioridade.ALTA,
        date.today() + timedelta(days=2),
    )
    sistema.criar_tarefa(
        projeto.id,
        "Publicar no GitHub",
        "Enviar o projeto e conferir o README.",
        Prioridade.MEDIA,
        date.today() + timedelta(days=3),
    )

    tarefa_modelagem.marcar_concluida()
    tarefa_codigo.iniciar()

    print("=== DEMONSTRAÇÃO DO PROJETO ===")
    print(usuario)
    print(projeto)
    print("\nTAREFAS")
    for tarefa in projeto.tarefas:
        print(f"- {tarefa}")
    print("\n" + sistema.gerar_relatorio_texto())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerenciador Inteligente de Tarefas")
    parser.add_argument("--demo", action="store_true", help="executa um cenário automático")
    argumentos = parser.parse_args()
    executar_demonstracao() if argumentos.demo else executar_menu()

