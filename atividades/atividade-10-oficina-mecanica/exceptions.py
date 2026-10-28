class DadosInvalidosError(ValueError):
    """Indica que um dado informado não atende às regras do sistema."""


class ItemNaoEncontradoError(LookupError):
    """Indica que um veículo ou uma ordem não foi encontrado."""

