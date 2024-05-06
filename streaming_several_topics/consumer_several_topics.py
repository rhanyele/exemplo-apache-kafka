from confluent_kafka import Consumer, KafkaError

# Configurações do Kafka
bootstrap_servers = 'localhost:29092'
topicos = ['meu_topico1', 'meu_topico2', 'meu_topico3']  # Lista de tópicos

# Configurações do consumidor
# 'auto.offset.reset': 'earliest' = o consumidor começará a ler do início do tópico.
# 'auto.offset.reset': 'latest' = o consumidor começará a ler mensagens que são produzidas após a conexão do consumidor ao tópico.
consumer_conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'meu_grupo',
    'auto.offset.reset': 'earliest'  # Lê do início do tópico
}

def callback(msg):
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            return
        else:
            print(f'Erro ao consumir mensagem: {msg.error()}')
            return
    print(f'Mensagem consumida do tópico {msg.topic()}: {msg.value().decode("utf-8")}')

def consumir_mensagens():
    c = Consumer(consumer_conf)
    c.subscribe(topicos)

    try:
        while True:
            msg = c.poll(timeout=1.0)
            if msg is None:
                continue
            callback(msg)
    except KeyboardInterrupt:
        pass
    finally:
        c.close()

if __name__ == "__main__":
    consumir_mensagens()