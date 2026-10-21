package br.com.fitlife.exception;

/** Exceção de regra de negócio para dados inválidos. */
public class DadosInvalidosException extends RuntimeException {
    public DadosInvalidosException(String mensagem) {
        super(mensagem);
    }
}
