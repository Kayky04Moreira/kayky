import unittest

from exceptions import DadosInvalidosError, ItemNaoEncontradoError
from oficina import Oficina
from ordem_servico import OrdemServico
from servico import Alinhamento, Servico, TrocaOleo
from veiculo import Veiculo


class TestVeiculo(unittest.TestCase):
    def test_cria_veiculo_com_placa_mercosul(self):
        veiculo = Veiculo("abc1d23", "Civic", 2022)
        self.assertEqual(veiculo.placa, "ABC1D23")

    def test_aceita_placa_antiga_com_hifen(self):
        self.assertEqual(Veiculo("ABC-1234", "Gol", 2015).placa, "ABC1234")

    def test_rejeita_placa_invalida(self):
        with self.assertRaises(DadosInvalidosError):
            Veiculo("123", "Gol", 2015)

    def test_rejeita_modelo_vazio(self):
        with self.assertRaises(DadosInvalidosError):
            Veiculo("ABC1234", "", 2015)

    def test_rejeita_ano_fora_da_faixa(self):
        with self.assertRaises(DadosInvalidosError):
            Veiculo("ABC1234", "Gol", 1800)


class TestServicos(unittest.TestCase):
    def test_servico_e_abstrato(self):
        with self.assertRaises(TypeError):
            Servico("Genérico", 10)

    def test_troca_oleo_calcula_total(self):
        self.assertEqual(TrocaOleo(80, 170).calcular_valor(), 250)

    def test_alinhamento_calcula_total(self):
        self.assertEqual(Alinhamento(90, 60).calcular_valor(), 150)

    def test_rejeita_valor_negativo(self):
        with self.assertRaises(DadosInvalidosError):
            TrocaOleo(-1, 100)


class TestOrdemServico(unittest.TestCase):
    def setUp(self):
        self.veiculo = Veiculo("ABC1D23", "Civic", 2022)
        self.ordem = OrdemServico(1, "Kayky", self.veiculo)

    def test_ordem_comeca_sem_servicos(self):
        self.assertEqual(self.ordem.calcular_total(), 0)

    def test_adiciona_servicos_e_calcula_total(self):
        self.ordem.adicionar_servico(TrocaOleo(80, 170))
        self.ordem.adicionar_servico(Alinhamento(90, 60))
        self.assertEqual(self.ordem.calcular_total(), 400)

    def test_servicos_sao_expostos_como_tupla(self):
        self.assertIsInstance(self.ordem.servicos, tuple)

    def test_resumo_contem_cliente_veiculo_e_total(self):
        resumo = self.ordem.resumo()
        self.assertIn("Kayky", resumo)
        self.assertIn("ABC1D23", resumo)
        self.assertIn("TOTAL: R$ 0.00", resumo)

    def test_rejeita_cliente_vazio(self):
        with self.assertRaises(DadosInvalidosError):
            OrdemServico(1, "", self.veiculo)


class TestOficina(unittest.TestCase):
    def setUp(self):
        self.oficina = Oficina("Oficina POO")
        self.veiculo = Veiculo("ABC1D23", "Civic", 2022)
        self.oficina.cadastrar_veiculo(self.veiculo)

    def test_cadastra_e_busca_veiculo(self):
        self.assertIs(self.oficina.buscar_veiculo("abc1d23"), self.veiculo)

    def test_impede_placa_duplicada(self):
        with self.assertRaises(DadosInvalidosError):
            self.oficina.cadastrar_veiculo(Veiculo("ABC1D23", "Outro", 2020))

    def test_busca_veiculo_inexistente(self):
        with self.assertRaises(ItemNaoEncontradoError):
            self.oficina.buscar_veiculo("XYZ9Z99")

    def test_abre_ordem_com_numeracao_sequencial(self):
        primeira = self.oficina.abrir_ordem("Ana", "ABC1D23")
        segunda = self.oficina.abrir_ordem("Bruno", "ABC1D23")
        self.assertEqual((primeira.numero, segunda.numero), (1, 2))

    def test_adiciona_servico_na_ordem(self):
        ordem = self.oficina.abrir_ordem("Ana", "ABC1D23")
        self.oficina.adicionar_servico(ordem.numero, TrocaOleo(50, 100))
        self.assertEqual(ordem.calcular_total(), 150)

    def test_busca_ordem_inexistente(self):
        with self.assertRaises(ItemNaoEncontradoError):
            self.oficina.buscar_ordem(99)


if __name__ == "__main__":
    unittest.main()

