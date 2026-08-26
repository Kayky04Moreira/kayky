from enum import IntEnum


class Prioridade(IntEnum):
    """Níveis de prioridade aceitos para uma tarefa."""

    BAIXA = 1
    MEDIA = 2
    ALTA = 3
    URGENTE = 4

    def __str__(self) -> str:
        return self.name

