import re

from exceptions import DadosInvalidosError


class Veiculo:
    """Representa um veículo cadastrado na oficina."""

    _PADRAO_PLACA = re.compile(r"^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$")

    def __init__(self, placa: str, modelo: str, ano: int):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano

    @property
    def placa(self) -> str:
        return self._placa

    @placa.setter
    def placa(self, valor: str) -> None:
        placa = str(valor).strip().upper().replace("-", "")
        if not self._PADRAO_PLACA.fullmatch(placa):
            raise DadosInvalidosError(
                "A placa deve seguir o padrão ABC1234 ou Mercosul ABC1D23."
            )
        self._placa = placa

    @property
    def modelo(self) -> str:
        return self._modelo

    @modelo.setter
    def modelo(self, valor: str) -> None:
        modelo = str(valor).strip()
        if len(modelo) < 2:
            raise DadosInvalidosError("O modelo do veículo deve ser informado.")
        self._modelo = modelo

    @property
    def ano(self) -> int:
        return self._ano

    @ano.setter
    def ano(self, valor: int) -> None:
        try:
            ano = int(valor)
        except (TypeError, ValueError) as erro:
            raise DadosInvalidosError("O ano deve ser um número inteiro.") from erro
        if not 1886 <= ano <= 2100:
            raise DadosInvalidosError("O ano deve estar entre 1886 e 2100.")
        self._ano = ano

    def __str__(self) -> str:
        return f"{self.modelo} ({self.ano}) - placa {self.placa}"

