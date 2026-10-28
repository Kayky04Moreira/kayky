# Explicação da solução

O sistema separa cada responsabilidade em uma classe. `Veiculo` guarda e valida placa,
modelo e ano. `Servico` é uma classe abstrata: ela define o contrato comum e obriga cada
tipo concreto a implementar `calcular_valor`. `TrocaOleo` e `Alinhamento` usam polimorfismo,
pois calculam seus preços de maneiras diferentes por meio do mesmo método.

`OrdemServico` associa um cliente e um veículo a vários serviços e soma o orçamento.
`Oficina` centraliza cadastros e buscas. As propriedades protegem os atributos, e as
exceções personalizadas geram mensagens compreensíveis quando os dados são inválidos.
O `main.py` oferece o menu solicitado e também o modo `--demo` para uma verificação rápida.

