package br.com.fitlife.model;

/** Plano mensal com cobrança igual ao valor base. */
public final class PlanoMensal extends Plano {
    public PlanoMensal(int id, double valorBase) {
        super(id, "Mensal", valorBase);
    }

    @Override
    public double calcularMensalidade() {
        return getValorBase();
    }
}
