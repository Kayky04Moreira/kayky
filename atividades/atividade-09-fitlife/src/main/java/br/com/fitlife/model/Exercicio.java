package br.com.fitlife.model;

import br.com.fitlife.exception.DadosInvalidosException;

/** Elemento que compõe um treino. */
public record Exercicio(String nome, int series, int repeticoes) {
    public Exercicio {
        if (nome == null || nome.isBlank()) {
            throw new DadosInvalidosException("O nome do exercício é obrigatório.");
        }
        nome = nome.trim();
        if (series <= 0 || repeticoes <= 0) {
            throw new DadosInvalidosException("Séries e repetições devem ser positivas.");
        }
    }

    @Override
    public String toString() {
        return "%s - %dx%d".formatted(nome, series, repeticoes);
    }
}
