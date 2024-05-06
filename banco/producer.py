from confluent_kafka import Producer
import json
import time

def delivery_report(err, msg):
    """Callback chamado quando a mensagem é entregue com sucesso ou falha."""
    if err is not None:
        print(f'Falha ao entregar mensagem: {err}')
    else:
        print(f'Mensagem entregue com sucesso: {msg.value().decode("utf-8")}')

def main():
    # Configurações do Kafka
    bootstrap_servers = 'localhost:29092'
    topic = 'meu_topico_postgres'

    # Inicializa o produtor Kafka
    producer = Producer({'bootstrap.servers': bootstrap_servers})

    try:
        # Produz mensagens e as envia para o Kafka
        for i in range(10):
            mensagem = {'id': i, 'conteudo': f'Mensagem {i}'}
            producer.produce(topic, value=json.dumps(mensagem), callback=delivery_report)
            time.sleep(1)  # Simula um intervalo de 1 segundo entre as mensagens
        # Espera todas as mensagens serem entregues
        producer.flush()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
