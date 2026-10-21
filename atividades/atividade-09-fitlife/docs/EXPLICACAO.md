# Explicação da solução

## Conceitos de POO aplicados

- **Classes e objetos:** Cliente, Plano, Treino, Exercicio, Pagamento e serviços representam o domínio da academia.
- **Encapsulamento:** os atributos são privados e só podem ser alterados por métodos que aplicam validações.
- **Herança:** PlanoMensal e PlanoPremium herdam os dados e comportamentos comuns da classe abstrata Plano.
- **Interface:** Calculavel define o contrato do cálculo de mensalidade.
- **Polimorfismo:** cada tipo de plano calcula a mensalidade de uma maneira, embora todos sejam tratados como Plano ou Calculavel.
- **Associação:** Cliente mantém referência ao Plano escolhido.
- **Agregação:** AcademiaService organiza clientes e planos que podem ser tratados como objetos independentes.
- **Composição:** Cliente possui treinos, e Treino possui exercícios.
- **Dependência:** PagamentoService usa Cliente e Plano apenas durante o processamento.
- **Exceções:** dados inválidos e falhas de pagamento produzem mensagens claras sem interromper o sistema de forma inesperada.

## Fluxo principal

1. Os planos Mensal e Premium são cadastrados.
2. O cliente é validado e cadastrado.
3. Um plano ativo é associado ao cliente.
4. O treino e seus exercícios são cadastrados.
5. PagamentoService solicita ao plano o valor polimórfico da mensalidade.
6. O pagamento aprovado e os dados do cliente são apresentados no console.
7. Os testes automatizados verificam regras válidas e inválidas.
