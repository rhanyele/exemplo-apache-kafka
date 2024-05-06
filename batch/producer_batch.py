from confluent_kafka import Producer
import time

class BatchProducer:
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers
        self.producer = Producer({'bootstrap.servers': self.bootstrap_servers})
        self.batch_size = 10  # Tamanho do lote
        self.message_buffer = []  # Buffer para armazenar as mensagens

    def send_message(self, topic, message):
        self.message_buffer.append((topic, message))  # Adiciona a mensagem ao buffer
        if len(self.message_buffer) >= self.batch_size:
            self.flush()  # Envia o lote se o buffer estiver cheio

    def flush(self):
        for topic, message in self.message_buffer:
            self.producer.produce(topic, message.encode('utf-8'))
        self.producer.flush()  # Envia as mensagens para o Kafka
        self.message_buffer = []  # Limpa o buffer

if __name__ == "__main__":
    producer = BatchProducer('localhost:29092')
    topic = 'meu_topico_batch'

    for i in range(100):
        message = f'Mensagem {i}'
        producer.send_message(topic, message)
        #time.sleep(0.1)  # Simula a produção de mensagens com um intervalo de 100 ms
