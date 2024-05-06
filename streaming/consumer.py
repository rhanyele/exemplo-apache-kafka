from confluent_kafka import Consumer

# Configurações do Kafka
bootstrap_servers = 'localhost:29092'
topic = 'meu_topico'

# Configurações do consumidor
consumer_conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'meu_grupo',
    'auto.offset.reset': 'earliest'
}

def consumir_mensagem():
    c = Consumer(consumer_conf)
    c.subscribe([topic])
    while True:
        msg = c.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            print(f'Erro ao consumir a mensagem: {msg.error()}')
            continue
        print(f'Recebida mensagem: {msg.value().decode("utf-8")}')

if __name__ == "__main__":
    consumir_mensagem()
