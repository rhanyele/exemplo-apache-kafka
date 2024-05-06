from confluent_kafka import Producer

# Configurações do Kafka
bootstrap_servers = 'localhost:29092'
topic = 'meu_topico'

# Configurações do produtor
producer_conf = {'bootstrap.servers': bootstrap_servers}

def delivery_report(err, msg):
    if err is not None:
        print(f'Erro ao entregar a mensagem: {err}')
    else:
        print(f'Mensagem entregue ao tópico {msg.topic()} - Partição {msg.partition()}')

def produzir_mensagem():
    p = Producer(producer_conf)
    value = 'Mensagem de teste'
    p.produce(topic, value.encode('utf-8'), callback=delivery_report)
    p.flush()

if __name__ == "__main__":
    produzir_mensagem()
