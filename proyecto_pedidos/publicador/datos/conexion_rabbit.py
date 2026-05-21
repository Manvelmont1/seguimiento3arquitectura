import pika

class ConexionRabbit:
    EXCHANGE = "pedidos_exchange"
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
        return True
    
    def enviar_mensaje(self, mensaje):
        self.channel.basic_publish(
            exchange=self.EXCHANGE,
            routing_key=self.ROUTING_KEY,
            body=mensaje.encode("utf-8"),
            properties=pika.BasicProperties(delivery_mode=2)
        )
        return True
    
    def desconectar(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()
            