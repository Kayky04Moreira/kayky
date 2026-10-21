package br.com.fitlife.model;

import org.junit.jupiter.api.Test;
import java.util.List;
import static org.junit.jupiter.api.Assertions.assertEquals;

class PlanoTest {
    @Test
    void deveCalcularPlanoMensal() {
        assertEquals(100.0, new PlanoMensal(1, 100.0).calcularMensalidade());
    }

    @Test
    void deveCalcularPlanoPremium() {
        assertEquals(250.0, new PlanoPremium(2, 200.0, 50.0).calcularMensalidade());
    }

    @Test
    void deveAplicarPolimorfismo() {
        List<Calculavel> planos = List.of(
                new PlanoMensal(1, 100.0),
                new PlanoPremium(2, 200.0, 50.0));
        assertEquals(350.0, planos.stream().mapToDouble(Calculavel::calcularMensalidade).sum());
    }
}
