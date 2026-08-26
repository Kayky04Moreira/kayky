# Gerenciador Inteligente de Tarefas

Projeto desenvolvido para a Aula 03 de Programação Orientada a Objetos. O sistema organiza usuários, projetos e tarefas, controla prioridades e status, calcula o progresso e produz relatórios de produtividade.

## Objetivo

Aplicar os fundamentos de POO em uma solução completa, modular e reutilizável. O projeto demonstra classes, objetos, atributos, métodos, encapsulamento, associações entre objetos e enumerações.

## Funcionalidades

- cadastro, listagem e remoção de usuários;
- criação, listagem e remoção de projetos por usuário;
- cadastro de tarefas com título, descrição, prioridade e data limite;
- estados `PENDENTE`, `EM ANDAMENTO` e `CONCLUÍDA`;
- prioridades `BAIXA`, `MÉDIA`, `ALTA` e `URGENTE`;
- identificação automática de tarefas vencidas;
- cálculo do percentual de conclusão de cada projeto;
- relatório de tarefas pendentes por prioridade;
- ranking de projetos por percentual de conclusão;
- total de tarefas concluídas por usuário;
- exportação opcional dos relatórios para TXT e CSV;
- menu interativo no terminal e demonstração automática;
- testes automatizados das principais regras de negócio.

## Modelagem

```text
Usuario 1 ───── * Projeto 1 ───── * Tarefa
                                      │
                                      ├── Prioridade (enum)
                                      └── Status (enum)
```

- `Usuario` mantém seus projetos.
- `Projeto` mantém suas tarefas e calcula o progresso.
- `Tarefa` controla prioridade, prazo e status.
- `GerenciadorTarefas` coordena cadastros, consultas, relatórios e exportações.

## Tecnologias utilizadas

- Python 3.11 ou superior;
- biblioteca padrão do Python;
- `unittest` para testes automatizados;
- nenhuma dependência externa para executar o sistema.

## Estrutura do projeto

```text
projeto-gerenciador-tarefas/
├── main.py                      # Ponto de entrada e menu
├── README.md                    # Documentação
├── src/
│   ├── enums/
│   │   ├── prioridade.py
│   │   └── status.py
│   ├── models/
│   │   ├── usuario.py
│   │   ├── projeto.py
│   │   └── tarefa.py
│   └── services/
│       └── gerenciador.py
├── tests/
│   └── test_sistema.py
└── exports/                     # Relatórios TXT e CSV
```

## Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/Kayky04Moreira/kayky.git
   cd kayky
   ```

2. Execute o menu interativo:

   ```bash
   python main.py
   ```

3. Para visualizar um cenário pronto:

   ```bash
   python main.py --demo
   ```

## Como executar os testes

```bash
python -m unittest discover -s tests -v
```

## Exemplo de uso

```text
=== DEMONSTRAÇÃO DO PROJETO ===
#1 Kayky Moreira Assunção (...) - 1 projeto(s)
#1 Atividade de Programação Orientada a Objetos | progresso: 33.3%

TAREFAS
- #1 Modelar as classes | URGENTE | CONCLUÍDA
- #2 Implementar o sistema | ALTA | EM ANDAMENTO
- #3 Publicar no GitHub | MEDIA | PENDENTE
```

## Conceitos de POO aplicados

- **Abstração:** as classes representam entidades do problema real.
- **Encapsulamento:** os atributos são protegidos e alterados por métodos validados.
- **Associação:** usuários, projetos e tarefas mantêm referências entre si.
- **Composição:** projetos organizam suas tarefas e usuários organizam seus projetos.
- **Reutilização:** regras e relatórios ficam separados da interface de terminal.

## Autor

**Kayky Moreira Assunção**  
Ciência da Computação - 6º período - Noturno  
Programação Orientada a Objetos
