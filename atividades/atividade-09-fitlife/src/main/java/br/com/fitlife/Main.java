package br.com.fitlife;

import br.com.fitlife.exception.DadosInvalidosException;
import br.com.fitlife.model.Cliente;
import br.com.fitlife.model.Exercicio;
import br.com.fitlife.model.Pagamento;
import br.com.fitlife.model.Plano;
import br.com.fitlife.model.PlanoMensal;
import br.com.fitlife.model.PlanoPremium;
import br.com.fitlife.model.Treino;
import br.com.fitlife.service.AcademiaService;
import br.com.fitlife.service.PagamentoService;
import java.util.List;

/** Demonstração executável das funcionalidades exigidas na atividade. */
public final class Main {
    private Main() {
    }

    public static void main(String[] args) {
        AcademiaService academia = new AcademiaService();
        PagamentoService pagamentos = new PagamentoService();

        Plano mensal = new PlanoMensal(1, 100.00);
        Plano premium = new PlanoPremium(2, 200.00, 50.00);
        academia.cadastrarPlano(mensal);
        academia.cadastrarPlano(premium);

        Cliente kayky = academia.cadastrarCliente("Kayky Moreira Assunção", "kayky@fitlife.com", 22);
        Cliente mateus = academia.cadastrarCliente("Mateus Bonifácio Nolasco", "mateus@fitlife.com", 23);
        academia.associarPlano(kayky.getId(), premium.getId());
        academia.associarPlano(mateus.getId(), mensal.getId());

        Treino treinoA = new Treino("Treino A - Peito e tríceps");
        treinoA.adicionarExercicio(new Exercicio("Supino reto", 4, 10));
        treinoA.adicionarExercicio(new Exercicio("Tríceps na polia", 3, 12));
        academia.cadastrarTreino(kayky.getId(), treinoA);

        System.out.println("=== FITLIFE - DEMONSTRAÇÃO DO SISTEMA ===");
        System.out.println("\nPLANOS CADASTRADOS");
        academia.listarPlanos().forEach(plano ->
                System.out.printf("- %s: R$ %.2f%n", plano.getNome(), plano.calcularMensalidade()));

        System.out.println("\nCLIENTES E TREINOS");
        academia.listarClientes().forEach(cliente -> {
            System.out.println("- " + cliente);
            cliente.getTreinos().forEach(treino -> System.out.println("  " + treino));
        });

        System.out.println("\nPAGAMENTOS");
        for (Cliente cliente : List.of(kayky, mateus)) {
            Pagamento pagamento = pagamentos.processarPagamento(cliente);
            System.out.printf("- %s | %s | R$ %.2f | %s%n",
                    pagamento.cliente(), pagamento.plano(), pagamento.valor(), pagamento.status());
        }

        System.out.println("\nVALIDAÇÃO E TRATAMENTO DE ERRO");
        try {
            academia.cadastrarCliente("Aluno inválido", "email-invalido", 14);
        } catch (DadosInvalidosException erro) {
            System.out.println("- Erro tratado corretamente: " + erro.getMessage());
        }

        System.out.println("\nSistema executado com sucesso.");
    }
}
