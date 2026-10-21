package br.com.fitlife.model;

import br.com.fitlife.exception.DadosInvalidosException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.regex.Pattern;

/** Cliente da academia com dados encapsulados e validações. */
public final class Cliente {
    private static final Pattern EMAIL = Pattern.compile("^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$");

    private final int id;
    private String nome;
    private String email;
    private int idade;
    private Plano plano;
    private final List<Treino> treinos = new ArrayList<>();

    public Cliente(int id, String nome, String email, int idade) {
        if (id <= 0) {
            throw new DadosInvalidosException("O identificador do cliente deve ser positivo.");
        }
        this.id = id;
        setNome(nome);
        setEmail(email);
        setIdade(idade);
    }

    public int getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        if (nome == null || nome.isBlank()) {
            throw new DadosInvalidosException("O nome é obrigatório.");
        }
        this.nome = nome.trim();
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        if (email == null || !EMAIL.matcher(email.trim()).matches()) {
            throw new DadosInvalidosException("E-mail inválido.");
        }
        this.email = email.trim().toLowerCase();
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        if (idade < 15) {
            throw new DadosInvalidosException("A idade mínima é 15 anos.");
        }
        this.idade = idade;
    }

    public Plano getPlano() {
        return plano;
    }

    public void associarPlano(Plano plano) {
        if (plano == null || !plano.isAtivo()) {
            throw new DadosInvalidosException("É necessário escolher um plano ativo.");
        }
        this.plano = plano;
    }

    public void adicionarTreino(Treino treino) {
        if (treino == null) {
            throw new DadosInvalidosException("O treino não pode ser nulo.");
        }
        treinos.add(treino);
    }

    public List<Treino> getTreinos() {
        return Collections.unmodifiableList(treinos);
    }

    @Override
    public String toString() {
        String planoAtual = plano == null ? "sem plano" : plano.getNome();
        return "%d - %s | %s | %d anos | %s".formatted(id, nome, email, idade, planoAtual);
    }
}
