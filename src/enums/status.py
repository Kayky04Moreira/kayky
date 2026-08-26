from enum import Enum


class Status(str, Enum):
    """Situações possíveis no ciclo de vida de uma tarefa."""

    PENDENTE = "PENDENTE"
    EM_ANDAMENTO = "EM ANDAMENTO"
    CONCLUIDA = "CONCLUÍDA"

    def __str__(self) -> str:
        return self.value

