package br.com.fitlife.service;

import br.com.fitlife.exception.PagamentoException;
import br.com.fitlife.model.Cliente;
import br.com.fitlife.model.Pagamento;
import br.com.fitlife.model.PlanoMensal;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class PagamentoServiceTest {
    @Test
    void deveProcessarPagamento() {
        Cliente cliente = new Cliente(1, "Kayky", "kayky@email.com", 22);
        cliente.associarPlano(new PlanoMensal(1, 100.0));
        Pagamento pagamento = new PagamentoService().processarPagamento(cliente);
        assertEquals("APROVADO", pagamento.status());
        assertEquals(100.0, pagamento.valor());
    }

    @Test
    void naoDeveProcessarClienteSemPlano() {
        Cliente cliente = new Cliente(1, "Kayky", "kayky@email.com", 22);
        assertThrows(PagamentoException.class,
                () -> new PagamentoService().processarPagamento(cliente));
    }

    @Test
    void naoDeveProcessarPlanoInativo() {
        Cliente cliente = new Cliente(1, "Kayky", "kayky@email.com", 22);
        PlanoMensal plano = new PlanoMensal(1, 100.0);
        cliente.associarPlano(plano);
        plano.desativar();
        assertThrows(PagamentoException.class,
                () -> new PagamentoService().processarPagamento(cliente));
    }
}
