# Projeto Exemplo Apache Kafka

Kafka é uma plataforma de streaming distribuída normalmente usada para construir pipelines de dados em tempo real, mas pode ser adaptada para diferentes cenários.

O projeto é uma aplicação Python utilizando o Apache Kafka, criada para ser um exemplo das funcionalidades básicas do Kafka. Este projeto tem como objetivo ser uma referência para projetos posteriores com a ferramenta.

No Apache Kafka, um consumer é um programa que lê dados de um tópico (um canal de comunicação) e os processa. É como um receptor de mensagens em uma fila de correio. Enquanto isso, um producer é um programa que envia dados para um tópico. É como o remetente de mensagens na fila de correio. Em resumo, os consumers consomem (leem) dados e os producers produzem (enviam) dados no Kafka.

![Visão Geral do Apache Kafka](https://github.com/rhanyele/exemplo-apache-kafka/assets/10997593/c7a2ab47-50a0-4ea4-9132-889c9f6f57b3)

### Documentação
- [Apache Kafka](https://kafka.apache.org/)

## Estrutura do projeto
```bash
- batch
  - consumer_batch.py
  - producer_batch.py
- database
  - .env
  - consumer_database.py
  - producer_database.py
- streaming
  - consumer.py
  - producer.py
- streaming_several_topics
  - consumer_several_topics.py
  - producer_several_topics.py
- topic
  - create_topic.py
  - delete_topic.py
  - list_topic.py
  - messages_topic.py
- docker-compose.yml
```

## Funcionalidades
- **Criar topico:** Cria um novo tópico no Kafka.
- **Deletar topico:** Deleta um tópico no Kafka.
- **Listar topicos:** Lista todos os tópicos do Kafka.
- **Mensagens topico:** Carrega todas as mensagens já enviadas em um tópico do Kafka, as mensagens ficam disponiveis em um tópico conforme as configurações de tempo de retenção e tamanho máximo.
- **Consumer:** Consome/Lê as mensagens de dentro de um tópico.
- **Producer:** Produz e envia as mensagens para dentro de um tópico.

## Requisitos
- Python
- Poetry
- Docker

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/rhanyele/exemplo-apache-kafka.git
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd exemplo-apache-kafka
   ```

3. Instale as dependências usando Poetry:
   ```bash
   poetry install
   ```
   
4. Execute o Docker Composer:

   ```bash
   docker compose up -d
   ```

5. Na pasta database, crie um arquivo `.env` com as variáveis de conexão do seu banco de dados PostgreSQL:
   ```
   DB_HOST=seu_host
   DB_PORT=sua_porta
   DB_NAME=seu_banco_de_dados
   DB_USER=seu_usuario
   DB_PASS=sua_senha
   ```

## Uso
### Topic
Cria um tópico no Kafka para a comunicação entre os producers e consumers. Você pode criar quantos tópicos forem necessários.
```bash
poetry run python .\topic\create_topic.py 
```

Deleta um tópico no Kafka.
```bash
poetry run python .\topic\delete_topic.py 
```

Lista todos os tópicos do Kafka.
```bash
poetry run python .\topic\list_topic.py 
```

Lê todas as mensagens enviadas em um tópico no Kafka.
```bash
poetry run python .\topic\messages_topic.py 
```

### Streaming
Cria um producer que vai enviar mensagens para um tópico no Kafka.
```bash
poetry run python .\streaming\producer.py 
```

Cria um consumer que vai consumir/ler as mensagens de um tópico no Kafka.
```bash
poetry run python .\streaming\consumer.py 
```

### Batch
Cria um producer que vai enviar um lote de mensagens para um tópico no Kafka.
```bash
poetry run python .\batch\producer_batch.py 
```

Cria um consumer que vai consumir/ler as mensagens em lote de um tópico no Kafka.
```bash
poetry run python .\batch\consumer_batch.py 
```

### Database
Cria um producer que vai enviar 10 mensagens seguidas para um tópico no Kafka.
```bash
poetry run python .\database\producer_database.py 
```

Cria um consumer que vai consumir/ler as mensagens de um tópico no Kafka e salvar no banco de dados PostreSQL.
```bash
poetry run python .\database\consumer_database.py 
```

### Streaming several topics
Cria um producer que vai enviar mensagem para vários tópicos no Kafka.
```bash
poetry run python .\streaming_several_topics\producer_several_topics.py 
```

Cria um consumer que vai consumir/ler as mensagens de vários tópico no Kafka.
```bash
poetry run python .\streaming_several_topics\consumer_several_topics.py 
```

## Autor
[Rhanyele Teixeira Nunes Marinho](https://github.com/rhanyele)

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).
