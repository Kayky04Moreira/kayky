from __future__ import annotations

from datetime import date

from src.models.projeto import Projeto


class Usuario:
    """Representa uma pessoa que pode possuir vários projetos."""

    def __init__(self, identificador: int, nome: str, email: str, senha: str) -> None:
        if not nome.strip():
            raise ValueError("O nome do usuário não pode ser vazio.")
        if "@" not in email:
            raise ValueError("Informe um e-mail válido.")
        if len(senha) < 4:
            raise ValueError("A senha deve possuir pelo menos quatro caracteres.")

        self.__id = identificador
        self.__nome = nome.strip()
        self.__email = email.strip().lower()
        self.__senha = senha
        self.__projetos: list[Projeto] = []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def email(self) -> str:
        return self.__email

    @property
    def projetos(self) -> tuple[Projeto, ...]:
        return tuple(self.__projetos)

    def validar_senha(self, senha: str) -> bool:
        return self.__senha == senha

    def criar_projeto(
        self,
        identificador: int,
        nome: str,
        descricao: str,
        data_criacao: date | None = None,
    ) -> Projeto:
        projeto = Projeto(identificador, nome, descricao, self, data_criacao)
        self.__projetos.append(projeto)
        return projeto

    def listar_projetos(self) -> tuple[Projeto, ...]:
        return self.projetos

    def remover_projeto(self, identificador: int) -> Projeto:
        projeto = self.buscar_projeto(identificador)
        self.__projetos.remove(projeto)
        return projeto

    def buscar_projeto(self, identificador: int) -> Projeto:
        for projeto in self.__projetos:
            if projeto.id == identificador:
                return projeto
        raise ValueError("Projeto não encontrado para este usuário.")

    def __str__(self) -> str:
        return f"#{self.id} {self.nome} ({self.email}) - {len(self.projetos)} projeto(s)"

