from confluent_kafka.admin import AdminClient, NewTopic
from datetime import datetime, timedelta

def criar_topico_com_config(nome, num_partitions=1, replication_factor=1, retention_ms=None, retention_bytes=None):
    # Configurações do Kafka
    bootstrap_servers = 'localhost:29092'

    # Configurações do cliente administrativo
    conf = {'bootstrap.servers': bootstrap_servers}

    # Cria um cliente administrativo
    admin_client = AdminClient(conf)

    # Configurações adicionais para o tópico (retenção de tempo e tamanho)
    config = {'retention.ms': retention_ms, 'retention.bytes': retention_bytes}

    # Cria o objeto NewTopic com configurações adicionais
    new_topic = NewTopic(
        topic=nome,
        num_partitions=num_partitions,
        replication_factor=replication_factor,
        config=config
    )

    # Cria o tópico
    admin_client.create_topics([new_topic])

    print(f"Tópico '{nome}' criado com sucesso!")

if __name__ == "__main__":
    nome_do_topico = "meu_topico_postgres"
    num_de_partitions = 1
    fator_de_replicacao = 1

    # Tempo de retenção: 7 dias (em milissegundos)
    tempo_de_retencao_ms = timedelta(days=7).total_seconds() * 1000

    # Tamanho máximo do log: 1 GB
    tamanho_maximo_do_log_bytes = 1024 * 1024 * 1024  # 1 GB

    criar_topico_com_config(nome_do_topico, num_de_partitions, fator_de_replicacao, tempo_de_retencao_ms, tamanho_maximo_do_log_bytes)
