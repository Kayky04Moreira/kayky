package br.com.fitlife.model;

/** Plano premium com taxa de serviços adicionais. */
public final class PlanoPremium extends Plano {
    private final double taxaPremium;

    public PlanoPremium(int id, double valorBase, double taxaPremium) {
        super(id, "Premium", valorBase);
        if (taxaPremium < 0) {
            throw new IllegalArgumentException("A taxa premium não pode ser negativa.");
        }
        this.taxaPremium = taxaPremium;
    }

    public double getTaxaPremium() {
        return taxaPremium;
    }

    @Override
    public double calcularMensalidade() {
        return getValorBase() + taxaPremium;
    }
}
