package br.com.fitlife.model;

import br.com.fitlife.exception.DadosInvalidosException;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ClienteTest {
    @Test
    void deveCadastrarClienteValido() {
        Cliente cliente = new Cliente(1, "Kayky Moreira", "kayky@email.com", 22);
        assertEquals("Kayky Moreira", cliente.getNome());
        assertEquals("kayky@email.com", cliente.getEmail());
    }

    @Test
    void naoDeveCadastrarNomeVazio() {
        assertThrows(DadosInvalidosException.class,
                () -> new Cliente(1, " ", "kayky@email.com", 22));
    }

    @Test
    void naoDeveCadastrarEmailInvalido() {
        assertThrows(DadosInvalidosException.class,
                () -> new Cliente(1, "Kayky", "email-invalido", 22));
    }

    @Test
    void naoDeveCadastrarMenorDeQuinzeAnos() {
        assertThrows(DadosInvalidosException.class,
                () -> new Cliente(1, "Kayky", "kayky@email.com", 14));
    }

    @Test
    void deveAssociarPlanoEAdicionarTreino() {
        Cliente cliente = new Cliente(1, "Kayky", "kayky@email.com", 22);
        Plano plano = new PlanoMensal(1, 100.0);
        Treino treino = new Treino("Treino A");
        cliente.associarPlano(plano);
        cliente.adicionarTreino(treino);
        assertSame(plano, cliente.getPlano());
        assertEquals(1, cliente.getTreinos().size());
    }
}
