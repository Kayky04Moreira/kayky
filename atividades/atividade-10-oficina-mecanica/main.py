import argparse

from exceptions import DadosInvalidosError, ItemNaoEncontradoError
from oficina import Oficina
from servico import Alinhamento, TrocaOleo
from veiculo import Veiculo


def moeda(valor: str) -> float:
    texto = valor.strip().replace("R$", "").replace(" ", "")
    if "," in texto:
        texto = texto.replace(".", "").replace(",", ".")
    return float(texto)


def cadastrar_veiculo(oficina: Oficina) -> None:
    placa = input("Placa: ")
    modelo = input("Modelo: ")
    ano = input("Ano: ")
    oficina.cadastrar_veiculo(Veiculo(placa, modelo, ano))
    print("Veículo cadastrado com sucesso.")


def abrir_ordem(oficina: Oficina) -> None:
    cliente = input("Nome do cliente: ")
    placa = input("Placa do veículo: ")
    ordem = oficina.abrir_ordem(cliente, placa)
    print(f"Ordem nº {ordem.numero} aberta com sucesso.")


def lancar_servico(oficina: Oficina) -> None:
    numero = int(input("Número da ordem: "))
    print("1. Troca de óleo\n2. Alinhamento")
    tipo = input("Tipo do serviço: ").strip()
    mao_de_obra = moeda(input("Valor da mão de obra: R$ "))
    if tipo == "1":
        materiais = moeda(input("Valor dos materiais: R$ "))
        servico = TrocaOleo(mao_de_obra, materiais)
    elif tipo == "2":
        equipamento = moeda(input("Taxa do equipamento: R$ "))
        servico = Alinhamento(mao_de_obra, equipamento)
    else:
        raise DadosInvalidosError("Tipo de serviço inválido.")
    oficina.adicionar_servico(numero, servico)
    print("Serviço lançado com sucesso.")


def listar_ordens(oficina: Oficina) -> None:
    if not oficina.ordens:
        print("Nenhuma ordem cadastrada.")
        return
    for ordem in oficina.ordens:
        print(f"OS {ordem.numero} | {ordem.cliente} | {ordem.veiculo.placa} | "
              f"R$ {ordem.calcular_total():.2f}")


def exibir_orcamento(oficina: Oficina) -> None:
    numero = int(input("Número da ordem: "))
    print("\n" + oficina.buscar_ordem(numero).resumo())


def demonstracao() -> None:
    oficina = Oficina("Oficina POO")
    oficina.cadastrar_veiculo(Veiculo("ABC1D23", "Honda Civic", 2022))
    ordem = oficina.abrir_ordem("Kayky Moreira Assunção", "ABC1D23")
    ordem.adicionar_servico(TrocaOleo(80, 170))
    ordem.adicionar_servico(Alinhamento(90, 60))
    print("=" * 52)
    print("SISTEMA DE OFICINA MECÂNICA - DEMONSTRAÇÃO")
    print("=" * 52)
    print(ordem.resumo())


def executar_menu() -> None:
    oficina = Oficina("Oficina POO")
    opcoes = {
        "1": cadastrar_veiculo,
        "2": abrir_ordem,
        "3": lancar_servico,
        "4": listar_ordens,
        "5": exibir_orcamento,
    }
    while True:
        print("\n=== SISTEMA DE OFICINA MECÂNICA ===")
        print("1. Cadastrar veículo")
        print("2. Abrir ordem de serviço")
        print("3. Lançar serviço")
        print("4. Listar ordens")
        print("5. Exibir orçamento")
        print("0. Sair")
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "0":
            print("Sistema encerrado.")
            break
        try:
            acao = opcoes.get(escolha)
            if acao is None:
                raise DadosInvalidosError("Opção inválida.")
            acao(oficina)
        except (DadosInvalidosError, ItemNaoEncontradoError, ValueError) as erro:
            print(f"Não foi possível concluir: {erro}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sistema de Oficina Mecânica")
    parser.add_argument("--demo", action="store_true", help="executa uma demonstração")
    argumentos = parser.parse_args()
    demonstracao() if argumentos.demo else executar_menu()

