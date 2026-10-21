package br.com.fitlife.service;

import br.com.fitlife.exception.PagamentoException;
import br.com.fitlife.model.Cliente;
import br.com.fitlife.model.Pagamento;
import br.com.fitlife.model.Plano;
import java.time.LocalDateTime;

/** Serviço de pagamento separado das entidades de domínio. */
public final class PagamentoService {
    public Pagamento processarPagamento(Cliente cliente) {
        if (cliente == null) {
            throw new PagamentoException("Cliente inválido.");
        }
        Plano plano = cliente.getPlano();
        if (plano == null) {
            throw new PagamentoException("O cliente não possui plano associado.");
        }
        if (!plano.isAtivo()) {
            throw new PagamentoException("O plano associado está inativo.");
        }

        double valor = plano.calcularMensalidade();
        if (valor <= 0) {
            throw new PagamentoException("O valor calculado para pagamento é inválido.");
        }
        return new Pagamento(cliente.getId(), cliente.getNome(), plano.getNome(), valor,
                LocalDateTime.now(), "APROVADO");
    }
}
