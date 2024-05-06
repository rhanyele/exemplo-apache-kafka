from confluent_kafka import Consumer, KafkaException, TopicPartition

def consumir_todas_mensagens(nome_do_topico):
    # Configurações do Kafka
    bootstrap_servers = 'localhost:29092'

    # Configurações do consumidor
    consumer_conf = {
        'bootstrap.servers': bootstrap_servers,
        'group.id': 'meu_grupo'
    }

    # Cria um consumidor
    consumer = Consumer(consumer_conf)

    # Obtém as partições do tópico
    metadata = consumer.list_topics()
    partitions = metadata.topics[nome_do_topico].partitions

    # Cria uma lista de TopicPartition a partir do dicionário de deslocamentos
    topic_partitions = [TopicPartition(nome_do_topico, p) for p in partitions]

    # Atribui cada TopicPartition ao deslocamento inicial
    for tp in topic_partitions:
        tp.offset = 0  # Define o deslocamento inicial

    # Atribui a lista de TopicPartition ao consumidor
    consumer.assign(topic_partitions)

    try:
        # Lê mensagens de cada TopicPartition
        for partition in partitions:
            while True:
                msg = consumer.poll(timeout=1.0)
                if msg is None:
                    break
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        break
                    else:
                        raise KafkaException(msg.error())
                print(f'Mensagem recebida: {msg.value().decode("utf-8")}')
    finally:
        consumer.close()

if __name__ == "__main__":
    nome_do_topico = "meu_topico_postgres"
    consumir_todas_mensagens(nome_do_topico)
