package br.com.fitlife.model;

import br.com.fitlife.exception.DadosInvalidosException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/** Treino do cliente, composto por exercícios. */
public final class Treino {
    private final String nome;
    private final List<Exercicio> exercicios = new ArrayList<>();

    public Treino(String nome) {
        if (nome == null || nome.isBlank()) {
            throw new DadosInvalidosException("O nome do treino é obrigatório.");
        }
        this.nome = nome.trim();
    }

    public String getNome() {
        return nome;
    }

    public void adicionarExercicio(Exercicio exercicio) {
        if (exercicio == null) {
            throw new DadosInvalidosException("O exercício não pode ser nulo.");
        }
        exercicios.add(exercicio);
    }

    public List<Exercicio> getExercicios() {
        return Collections.unmodifiableList(exercicios);
    }

    @Override
    public String toString() {
        return nome + ": " + exercicios;
    }
}
