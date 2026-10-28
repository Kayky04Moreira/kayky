from exceptions import DadosInvalidosError
from servico import Servico
from veiculo import Veiculo


class OrdemServico:
    """Associa cliente, veículo e os serviços de uma manutenção."""

    def __init__(self, numero: int, cliente: str, veiculo: Veiculo):
        cliente = str(cliente).strip()
        if not cliente:
            raise DadosInvalidosError("O nome do cliente é obrigatório.")
        if not isinstance(veiculo, Veiculo):
            raise DadosInvalidosError("A ordem precisa de um veículo válido.")
        self._numero = int(numero)
        self._cliente = cliente
        self._veiculo = veiculo
        self._servicos: list[Servico] = []

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def cliente(self) -> str:
        return self._cliente

    @property
    def veiculo(self) -> Veiculo:
        return self._veiculo

    @property
    def servicos(self) -> tuple[Servico, ...]:
        return tuple(self._servicos)

    def adicionar_servico(self, servico: Servico) -> None:
        if not isinstance(servico, Servico):
            raise DadosInvalidosError("Somente serviços válidos podem ser adicionados.")
        self._servicos.append(servico)

    def calcular_total(self) -> float:
        return sum(servico.calcular_valor() for servico in self._servicos)

    def resumo(self) -> str:
        linhas = [
            f"ORDEM DE SERVIÇO Nº {self.numero}",
            f"Cliente: {self.cliente}",
            f"Veículo: {self.veiculo}",
            "Serviços:",
        ]
        if not self.servicos:
            linhas.append("  (nenhum serviço lançado)")
        else:
            for indice, servico in enumerate(self.servicos, 1):
                linhas.append(f"  {indice}. {servico}")
        linhas.append(f"TOTAL: R$ {self.calcular_total():.2f}")
        return "\n".join(linhas)

