package br.com.fitlife.exception;

/** Exceção específica para falhas de pagamento. */
public class PagamentoException extends RuntimeException {
    public PagamentoException(String mensagem) {
        super(mensagem);
    }
}
