from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from src.enums import Prioridade, Status
from src.models.tarefa import Tarefa

if TYPE_CHECKING:
    from src.models.usuario import Usuario


class Projeto:
    """Agrupa tarefas e calcula o progresso do trabalho."""

    def __init__(
        self,
        identificador: int,
        nome: str,
        descricao: str,
        usuario: Usuario,
        data_criacao: date | None = None,
    ) -> None:
        if not nome.strip():
            raise ValueError("O nome do projeto não pode ser vazio.")

        self.__id = identificador
        self.__nome = nome.strip()
        self.__descricao = descricao.strip()
        self.__data_criacao = data_criacao or date.today()
        self.__usuario = usuario
        self.__tarefas: list[Tarefa] = []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def descricao(self) -> str:
        return self.__descricao

    @property
    def data_criacao(self) -> date:
        return self.__data_criacao

    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def tarefas(self) -> tuple[Tarefa, ...]:
        return tuple(self.__tarefas)

    def criar_tarefa(
        self,
        identificador: int,
        titulo: str,
        descricao: str,
        prioridade: Prioridade,
        data_limite: date,
    ) -> Tarefa:
        tarefa = Tarefa(
            identificador,
            titulo,
            descricao,
            prioridade,
            data_limite,
            self,
        )
        self.__tarefas.append(tarefa)
        return tarefa

    def adicionar_tarefa(self, tarefa: Tarefa) -> None:
        if tarefa.projeto is not self:
            raise ValueError("A tarefa pertence a outro projeto.")
        if any(item.id == tarefa.id for item in self.__tarefas):
            raise ValueError("Já existe uma tarefa com esse identificador.")
        self.__tarefas.append(tarefa)

    def remover_tarefa(self, identificador: int) -> Tarefa:
        tarefa = self.buscar_tarefa(identificador)
        self.__tarefas.remove(tarefa)
        return tarefa

    def buscar_tarefa(self, identificador: int) -> Tarefa:
        for tarefa in self.__tarefas:
            if tarefa.id == identificador:
                return tarefa
        raise ValueError("Tarefa não encontrada.")

    def calcular_progresso(self) -> float:
        if not self.__tarefas:
            return 0.0
        concluidas = sum(tarefa.status == Status.CONCLUIDA for tarefa in self.__tarefas)
        return concluidas / len(self.__tarefas) * 100

    def __str__(self) -> str:
        return (
            f"#{self.id} {self.nome} | responsável: {self.usuario.nome} | "
            f"{len(self.tarefas)} tarefa(s) | progresso: {self.calcular_progresso():.1f}%"
        )

