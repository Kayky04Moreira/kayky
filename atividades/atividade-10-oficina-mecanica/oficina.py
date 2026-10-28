from exceptions import DadosInvalidosError, ItemNaoEncontradoError
from ordem_servico import OrdemServico
from servico import Servico
from veiculo import Veiculo


class Oficina:
    """Fachada que gerencia veículos e ordens de serviço."""

    def __init__(self, nome: str):
        self.nome = str(nome).strip() or "Oficina"
        self._veiculos: dict[str, Veiculo] = {}
        self._ordens: list[OrdemServico] = []

    @property
    def veiculos(self) -> tuple[Veiculo, ...]:
        return tuple(self._veiculos.values())

    @property
    def ordens(self) -> tuple[OrdemServico, ...]:
        return tuple(self._ordens)

    def cadastrar_veiculo(self, veiculo: Veiculo) -> None:
        if not isinstance(veiculo, Veiculo):
            raise DadosInvalidosError("Veículo inválido.")
        if veiculo.placa in self._veiculos:
            raise DadosInvalidosError("Já existe um veículo com essa placa.")
        self._veiculos[veiculo.placa] = veiculo

    def buscar_veiculo(self, placa: str) -> Veiculo:
        chave = str(placa).strip().upper().replace("-", "")
        try:
            return self._veiculos[chave]
        except KeyError as erro:
            raise ItemNaoEncontradoError("Veículo não encontrado.") from erro

    def abrir_ordem(self, cliente: str, placa: str) -> OrdemServico:
        ordem = OrdemServico(len(self._ordens) + 1, cliente, self.buscar_veiculo(placa))
        self._ordens.append(ordem)
        return ordem

    def buscar_ordem(self, numero: int) -> OrdemServico:
        for ordem in self._ordens:
            if ordem.numero == int(numero):
                return ordem
        raise ItemNaoEncontradoError("Ordem de serviço não encontrada.")

    def adicionar_servico(self, numero_ordem: int, servico: Servico) -> None:
        self.buscar_ordem(numero_ordem).adicionar_servico(servico)

