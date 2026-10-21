package br.com.fitlife.model;

import br.com.fitlife.exception.DadosInvalidosException;

/** Classe abstrata que concentra os dados e regras comuns dos planos. */
public abstract class Plano implements Calculavel {
    private final int id;
    private String nome;
    private double valorBase;
    private boolean ativo;

    protected Plano(int id, String nome, double valorBase) {
        if (id <= 0) {
            throw new DadosInvalidosException("O identificador do plano deve ser positivo.");
        }
        this.id = id;
        setNome(nome);
        setValorBase(valorBase);
        this.ativo = true;
    }

    public int getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public final void setNome(String nome) {
        if (nome == null || nome.isBlank()) {
            throw new DadosInvalidosException("O nome do plano é obrigatório.");
        }
        this.nome = nome.trim();
    }

    public double getValorBase() {
        return valorBase;
    }

    public final void setValorBase(double valorBase) {
        if (valorBase <= 0) {
            throw new DadosInvalidosException("O valor do plano deve ser maior que zero.");
        }
        this.valorBase = valorBase;
    }

    public boolean isAtivo() {
        return ativo;
    }

    public void ativar() {
        ativo = true;
    }

    public void desativar() {
        ativo = false;
    }

    @Override
    public String toString() {
        return "%s (R$ %.2f)".formatted(nome, calcularMensalidade());
    }
}
