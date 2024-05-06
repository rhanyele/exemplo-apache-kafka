from confluent_kafka.admin import AdminClient

def listar_topicos():
    # Configurações do Kafka
    bootstrap_servers = 'localhost:29092'

    # Configurações do cliente administrativo
    conf = {'bootstrap.servers': bootstrap_servers}

    # Cria um cliente administrativo
    admin_client = AdminClient(conf)

    # Obtém os metadados dos tópicos
    topic_metadata = admin_client.list_topics(timeout=10)

    # Lista os tópicos
    topic_names = topic_metadata.topics.keys()
    print("Tópicos:")
    for topic_name in topic_names:
        print(topic_name)

if __name__ == "__main__":
    listar_topicos()
