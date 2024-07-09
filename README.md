# Assistente Virtual Baseado em Ontologia

Este repositório contém um assistente virtual baseado em ontologia, desenvolvido utilizando a plataforma Rasa. O assistente é capaz de entender e responder a comandos dos usuários utilizando uma ontologia personalizada para estruturar e interpretar o conhecimento.

## Estrutura do Repositório

- `data/`
  - `nlu.yml`: Contém os exemplos de treinamento para as intenções e entidades.
  - `stories.yml`: Define as histórias para treinar o fluxo de conversação do assistente.
- `domain.yml`: Define as intenções, entidades, slots, respostas e ações do assistente.
- `actions.py`: Contém as ações personalizadas para interagir com a ontologia.
- `config.yml`: Configurações do pipeline de NLU do Rasa.
- `models/`: Diretório onde os modelos treinados são armazenados.
- `tests/`: Contém os testes para avaliar o comportamento do assistente.

## Configuração e Instalação

### Pré-requisitos

- Python 3.9
- Rasa 3.1
- rdflib

### Treinamento do modelo

Para treinar o modelo, execute:

```bash
rasa train
```

### Executando o Assistente

1. Inicie o servidor de ações:

```bash
rasa run actions
```

2. Em outro terminal, inicie o shell do Rasa para interagir com o assistente:

```bash
rasa shell
```
