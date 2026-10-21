# FitLife - Implementação e validação do sistema

Atividade prática da Unidade 4 de Programação Orientada a Objetos.

## Integrantes

- Lucas Borges Marra
- João Pedro Rodrigues Silva
- Mateus Bonifácio Nolasco
- João Pedro Rodrigues Venâncio
- Kayky Moreira Assunção

## Objetivo

Implementar e testar um módulo funcional da academia FitLife, aplicando classes e objetos, encapsulamento, herança, polimorfismo, interface, relacionamentos, exceções e boas práticas.

## Funcionalidades entregues

- Cadastro de clientes com nome, e-mail e idade.
- Cadastro dos planos Mensal e Premium.
- Associação de um plano ativo a um cliente.
- Cadastro de treinos e exercícios.
- Processamento da mensalidade.
- Validação de dados e tratamento de erros.
- Demonstração completa no console.
- Testes automatizados com JUnit 5.
- Diagrama de classes e explicação técnica em `docs/`.

## Requisitos

- Java 17 ou superior.
- Apache Maven 3.9 ou superior.

## Repositório no GitHub

Código publicado em:

https://github.com/Kayky04Moreira/kayky/tree/main/atividades/atividade-09-fitlife

## Como executar

No terminal, dentro desta pasta:

```powershell
mvn clean test
mvn exec:java
```

O primeiro comando compila o projeto e executa os testes. O segundo apresenta a demonstração do sistema no console.

## Organização

- `src/main/java`: código-fonte do sistema.
- `src/test/java`: testes automatizados.
- `docs/DIAGRAMA_CLASSES.md`: diagrama de classes em Mermaid.
- `docs/EXPLICACAO.md`: descrição dos conceitos e do fluxo.
- `evidencias/`: saídas registradas dos testes e da demonstração.

## Conceitos avaliados

O projeto utiliza todos os conceitos pedidos no material: fundamentos de POO, encapsulamento, herança, polimorfismo, interface, associação, agregação, composição, dependência, tratamento de exceções, separação de responsabilidades e testes.
