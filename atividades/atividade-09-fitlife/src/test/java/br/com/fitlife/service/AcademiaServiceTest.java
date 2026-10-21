package br.com.fitlife.service;

import br.com.fitlife.exception.DadosInvalidosException;
import br.com.fitlife.model.Cliente;
import br.com.fitlife.model.PlanoMensal;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AcademiaServiceTest {
    @Test
    void deveCadastrarEAssociarPlanoAoCliente() {
        AcademiaService academia = new AcademiaService();
        academia.cadastrarPlano(new PlanoMensal(1, 100.0));
        Cliente cliente = academia.cadastrarCliente("Kayky", "kayky@email.com", 22);
        academia.associarPlano(cliente.getId(), 1);
        assertEquals("Mensal", cliente.getPlano().getNome());
    }

    @Test
    void naoDevePermitirEmailDuplicado() {
        AcademiaService academia = new AcademiaService();
        academia.cadastrarCliente("Kayky", "kayky@email.com", 22);
        assertThrows(DadosInvalidosException.class,
                () -> academia.cadastrarCliente("Outro", "kayky@email.com", 30));
    }
}
