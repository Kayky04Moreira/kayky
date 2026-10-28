# Sistema de Oficina Mecânica

Projeto prático da Unidade 4/Aula 16 de Programação Orientada a Objetos. O sistema cadastra
veículos, abre ordens de serviço, registra troca de óleo ou alinhamento, calcula orçamentos,
lista as ordens e trata dados inválidos por meio de exceções amigáveis.

## Conceitos aplicados

- classes e objetos;
- encapsulamento com propriedades;
- classe abstrata;
- herança e polimorfismo;
- associação e composição;
- exceções personalizadas;
- menu interativo no terminal;
- testes automatizados.

## Estrutura

```text
main.py                  menu e demonstração
veiculo.py               cadastro e validação do veículo
servico.py               classe abstrata e serviços concretos
ordem_servico.py         orçamento e resumo da ordem
oficina.py               gerenciamento dos dados
exceptions.py            exceções personalizadas
tests/test_sistema.py    testes automatizados
docs/                    diagrama e explicação
evidencias/              resultados de execução e testes
```

## Como executar

É necessário ter Python 3.10 ou superior. No terminal, dentro desta pasta:

```powershell
python main.py
```

Demonstração automática:

```powershell
python main.py --demo
```

Testes:

```powershell
python -m unittest discover -s tests -v
```

## Exemplo do fluxo manual

1. Escolha `1` para cadastrar um veículo.
2. Escolha `2` para abrir a ordem para a placa cadastrada.
3. Escolha `3` para lançar troca de óleo ou alinhamento.
4. Escolha `4` para listar as ordens.
5. Escolha `5` para visualizar o orçamento completo.
6. Escolha `0` para sair.

## Integrantes

- Lucas Borges Marra
- João Pedro Rodrigues Silva
- Mateus Bonifácio Nolasco
- João Pedro Rodrigues Venâncio
- Kayky Moreira Assunção — matrícula 406392088938

Curso: Ciência da Computação — 6º período noturno  
Disciplina: Programação Orientada a Objetos  
Professor: Cleidson Daniel

## Repositório

[Atividade 10 no GitHub](https://github.com/Kayky04Moreira/kayky/tree/main/atividades/atividade-10-oficina-mecanica)

