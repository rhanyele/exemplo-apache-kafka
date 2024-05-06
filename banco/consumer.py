from confluent_kafka import Consumer, KafkaException, KafkaError
import psycopg2
import json
import os
from dotenv import load_dotenv

def persistir_no_postgres(mensagem):
    """Persiste a mensagem no banco de dados PostgreSQL."""
    try:
        # Configurações do PostgreSQL
        load_dotenv()

        DB_HOST = os.getenv("DB_HOST")
        DB_PORT = os.getenv("DB_PORT")
        DB_USER = os.getenv("DB_USER") 
        DB_PASS = os.getenv("DB_PASS")
        DB_NAME = os.getenv("DB_NAME")

        conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASS, database=DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO mensagens (mensagem) VALUES (%s)", (mensagem['conteudo'],))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Erro ao persistir no PostgreSQL:", error)
    finally:
        cursor.close()
        conn.close()

def main():
    # Configurações do Kafka
    bootstrap_servers = 'localhost:29092'
    topic = 'meu_topico_postgres'

    # Inicializa o consumidor Kafka
    consumer = Consumer({
        'bootstrap.servers': bootstrap_servers,
        'group.id': 'meu_grupo',
        'auto.offset.reset': 'earliest'  # Lê do início do tópico
    })

    # Assina o tópico
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    break
                else:
                    raise KafkaException(msg.error())
            mensagem = json.loads(msg.value().decode('utf-8'))
            persistir_no_postgres(mensagem)  # Persiste a mensagem no PostgreSQL
            print(f'Recebida mensagem: {msg.value().decode("utf-8")}')
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == "__main__":
    main()
