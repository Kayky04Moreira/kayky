from abc import ABC, abstractmethod

from exceptions import DadosInvalidosError


def _validar_valor(valor: float, campo: str) -> float:
    try:
        numero = float(valor)
    except (TypeError, ValueError) as erro:
        raise DadosInvalidosError(f"{campo} deve ser um número.") from erro
    if numero < 0:
        raise DadosInvalidosError(f"{campo} não pode ser negativo.")
    return numero


class Servico(ABC):
    """Contrato abstrato para os serviços oferecidos pela oficina."""

    def __init__(self, descricao: str, mao_de_obra: float):
        descricao = str(descricao).strip()
        if not descricao:
            raise DadosInvalidosError("A descrição do serviço é obrigatória.")
        self._descricao = descricao
        self._mao_de_obra = _validar_valor(mao_de_obra, "Mão de obra")

    @property
    def descricao(self) -> str:
        return self._descricao

    @property
    def mao_de_obra(self) -> float:
        return self._mao_de_obra

    @abstractmethod
    def calcular_valor(self) -> float:
        """Retorna o preço final do serviço."""

    def __str__(self) -> str:
        return f"{self.descricao}: R$ {self.calcular_valor():.2f}"


class TrocaOleo(Servico):
    def __init__(self, mao_de_obra: float, valor_materiais: float):
        super().__init__("Troca de óleo", mao_de_obra)
        self._valor_materiais = _validar_valor(valor_materiais, "Materiais")

    @property
    def valor_materiais(self) -> float:
        return self._valor_materiais

    def calcular_valor(self) -> float:
        return self.mao_de_obra + self.valor_materiais


class Alinhamento(Servico):
    def __init__(self, mao_de_obra: float, taxa_equipamento: float):
        super().__init__("Alinhamento", mao_de_obra)
        self._taxa_equipamento = _validar_valor(
            taxa_equipamento, "Taxa do equipamento"
        )

    @property
    def taxa_equipamento(self) -> float:
        return self._taxa_equipamento

    def calcular_valor(self) -> float:
        return self.mao_de_obra + self.taxa_equipamento

