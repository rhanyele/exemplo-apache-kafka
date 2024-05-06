from confluent_kafka import Consumer, KafkaException
from confluent_kafka.admin import AdminClient, NewTopic
from datetime import datetime, timedelta
import time

# Configurações do consumidor
# 'auto.offset.reset': 'earliest' = o consumidor começará a ler do início do tópico.
# 'auto.offset.reset': 'latest' = o consumidor começará a ler mensagens que são produzidas após a conexão do consumidor ao tópico.
class BatchConsumer:
    def __init__(self, bootstrap_servers, group_id, topic):
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.topic = topic
        self.consumer = Consumer({
            'bootstrap.servers': self.bootstrap_servers,
            'group.id': self.group_id,
            'auto.offset.reset': 'earliest'  # Lê do início do tópico
        })
        self.batch_size = 10  # Tamanho do lote
        self.message_buffer = []  # Buffer para armazenar as mensagens

    def consume_messages(self):
        self.consumer.subscribe([self.topic])

        while True:
            msg = self.consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    break
                else:
                    raise KafkaException(msg.error())
            self.message_buffer.append(msg.value().decode('utf-8'))  # Adiciona a mensagem ao buffer

            if len(self.message_buffer) >= self.batch_size:
                self.process_batch()  # Processa o lote se o buffer estiver cheio

    def process_batch(self):
        print("Processando lote de mensagens:")
        for message in self.message_buffer:
            print(message)
        self.message_buffer = []  # Limpa o buffer

if __name__ == "__main__":
    bootstrap_servers = 'localhost:29092'
    group_id = 'meu_grupo'
    topic = 'meu_topico_batch'

    consumer = BatchConsumer(bootstrap_servers, group_id, topic)
    consumer.consume_messages()
