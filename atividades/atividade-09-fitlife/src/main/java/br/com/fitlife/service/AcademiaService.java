package br.com.fitlife.service;

import br.com.fitlife.exception.DadosInvalidosException;
import br.com.fitlife.model.Cliente;
import br.com.fitlife.model.Plano;
import br.com.fitlife.model.Treino;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/** Serviço responsável pelas regras de cadastro e associação da academia. */
public final class AcademiaService {
    private final Map<Integer, Cliente> clientes = new LinkedHashMap<>();
    private final Map<Integer, Plano> planos = new LinkedHashMap<>();
    private int proximoClienteId = 1;

    public void cadastrarPlano(Plano plano) {
        if (plano == null) {
            throw new DadosInvalidosException("O plano não pode ser nulo.");
        }
        if (planos.containsKey(plano.getId())) {
            throw new DadosInvalidosException("Já existe plano com esse identificador.");
        }
        planos.put(plano.getId(), plano);
    }

    public Cliente cadastrarCliente(String nome, String email, int idade) {
        boolean duplicado = clientes.values().stream()
                .anyMatch(cliente -> cliente.getEmail().equalsIgnoreCase(email));
        if (duplicado) {
            throw new DadosInvalidosException("Já existe cliente com esse e-mail.");
        }
        Cliente cliente = new Cliente(proximoClienteId++, nome, email, idade);
        clientes.put(cliente.getId(), cliente);
        return cliente;
    }

    public void associarPlano(int clienteId, int planoId) {
        buscarCliente(clienteId).associarPlano(buscarPlano(planoId));
    }

    public void cadastrarTreino(int clienteId, Treino treino) {
        buscarCliente(clienteId).adicionarTreino(treino);
    }

    public Cliente buscarCliente(int id) {
        Cliente cliente = clientes.get(id);
        if (cliente == null) {
            throw new DadosInvalidosException("Cliente não encontrado.");
        }
        return cliente;
    }

    public Plano buscarPlano(int id) {
        Plano plano = planos.get(id);
        if (plano == null) {
            throw new DadosInvalidosException("Plano não encontrado.");
        }
        return plano;
    }

    public List<Cliente> listarClientes() {
        return Collections.unmodifiableList(new ArrayList<>(clientes.values()));
    }

    public List<Plano> listarPlanos() {
        return Collections.unmodifiableList(new ArrayList<>(planos.values()));
    }
}
