package br.com.fitlife.model;

import java.time.LocalDateTime;

/** Registro imutável de um pagamento processado. */
public record Pagamento(int clienteId, String cliente, String plano, double valor,
                        LocalDateTime processadoEm, String status) {
}
