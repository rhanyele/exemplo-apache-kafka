from confluent_kafka.admin import AdminClient, NewTopic

def delete_topic(bootstrap_servers, topic_name):
    # Inicializa o cliente de administração Kafka
    admin_client = AdminClient({'bootstrap.servers': bootstrap_servers})

    # Cria uma lista de tópicos a serem excluídos
    topics = [topic_name]

    # Exclui os tópicos
    admin_client.delete_topics(topics)

    # Fecha o cliente de administração Kafka
    admin_client.close()

if __name__ == "__main__":
    bootstrap_servers = 'localhost:29092'
    topic_name = 'meu_topico'

    delete_topic(bootstrap_servers, topic_name)
