from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from src.enums import Prioridade, Status

if TYPE_CHECKING:
    from src.models.projeto import Projeto


class Tarefa:
    """Representa uma tarefa pertencente a um projeto."""

    def __init__(
        self,
        identificador: int,
        titulo: str,
        descricao: str,
        prioridade: Prioridade,
        data_limite: date,
        projeto: Projeto,
    ) -> None:
        if not titulo.strip():
            raise ValueError("O título da tarefa não pode ser vazio.")
        if data_limite < projeto.data_criacao:
            raise ValueError("A data limite não pode ser anterior à criação do projeto.")

        self.__id = identificador
        self.__titulo = titulo.strip()
        self.__descricao = descricao.strip()
        self.__prioridade = prioridade
        self.__data_limite = data_limite
        self.__status = Status.PENDENTE
        self.__projeto = projeto

    @property
    def id(self) -> int:
        return self.__id

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @property
    def prioridade(self) -> Prioridade:
        return self.__prioridade

    @property
    def data_limite(self) -> date:
        return self.__data_limite

    @property
    def status(self) -> Status:
        return self.__status

    @property
    def projeto(self) -> Projeto:
        return self.__projeto

    def iniciar(self) -> None:
        if self.__status == Status.CONCLUIDA:
            raise ValueError("Uma tarefa concluída não pode voltar para em andamento.")
        self.__status = Status.EM_ANDAMENTO

    def marcar_concluida(self) -> None:
        self.__status = Status.CONCLUIDA

    def reabrir(self) -> None:
        self.__status = Status.PENDENTE

    def esta_vencida(self, hoje: date | None = None) -> bool:
        data_referencia = hoje or date.today()
        return self.__status != Status.CONCLUIDA and self.__data_limite < data_referencia

    def __str__(self) -> str:
        vencida = " - VENCIDA" if self.esta_vencida() else ""
        return (
            f"#{self.id} {self.titulo} | {self.prioridade} | "
            f"{self.status} | limite: {self.data_limite:%d/%m/%Y}{vencida}"
        )

