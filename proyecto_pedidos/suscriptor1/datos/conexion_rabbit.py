import pika

class ConexionRabbit:
    EXCHANGE = "pedidos_exchange"
    QUEUE = "cola_sql"
    ROUTING_KEY = "pedidos_key"
    
    def __init__(self):
        self.connection = None
        self.channel = None
    
    def conectar(self):
        credentials = pika.PlainCredentials(
            username="ojbcnehb",
            password="xJw2qw5O8E7sVYTEYqP3u0aW_HfkjVvo"
        )
        parameters = pika.ConnectionParameters(
            host="shark.rmq.cloudamqp.com",
            port=5672,
            virtual_host="ojbcnehb",
            credentials=credentials
        )
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        
        self.channel.exchange_declare(
            exchange=self.EXCHANGE,
            exchange_type="direct",
            durable=True
        )
        
        self.channel.queue_declare(queue=self.QUEUE, durable=True)
        
        self.channel.queue_bind(
            exchange=self.EXCHANGE,
            queue=self.QUEUE,
            routing_key=self.ROUTING_KEY
        )
        return True
    
    def escuchar(self, callback):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue=self.QUEUE,
            on_message_callback=callback
        )
        print("Suscriptor 1 escuchando los mensajes")
        self.channel.start_consuming()
    