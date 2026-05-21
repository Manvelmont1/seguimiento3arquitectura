package datos;

import com.rabbitmq.client.*;
import negocio.Pedido;
import presentacion.VentanaSuscriptor;
import org.json.JSONObject;

public class ConexionRabbit {
    private static final String EXCHANGE = "pedidos_exchange";
    private static final String QUEUE = "cola_gui";
    private static final String ROUTING_KEY = "pedidos_key";
    private static final String HOST = "shark.rmq.cloudamqp.com";
    private static final String USER = "ojbcnehb";
    private static final String PASSWORD = "xJw2qw5O8E7sVYTEYqP3u0aW_HfkjVvo";
    private static final String VHOST = "ojbcnehb";

    public void conectarYEscuchar(VentanaSuscriptor ventana) throws Exception {
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost(HOST);
        factory.setUsername(USER);
        factory.setPassword(PASSWORD);
        factory.setVirtualHost(VHOST);
        factory.setPort(5672);

        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();

        channel.exchangeDeclare(EXCHANGE, "direct", true);
        channel.queueDeclare(QUEUE, true, false, false, null);
        channel.queueBind(QUEUE, EXCHANGE, ROUTING_KEY);

        channel.basicQos(1);

        DeliverCallback deliverCallback = (consumerTag, delivery) -> {
            String mensaje = new String(delivery.getBody(), "UTF-8");
            System.out.println("📨 Mensaje recibido: " + mensaje);

            JSONObject json = new JSONObject(mensaje);
            Pedido pedido = new Pedido(
                json.getString("sku"),
                json.getInt("cantidad"),
                json.getString("talla"),
                json.getString("color")
            );

            ventana.mostrarPedido(pedido);
            channel.basicAck(delivery.getEnvelope().getDeliveryTag(), false);
        };

        channel.basicConsume(QUEUE, false, deliverCallback, consumerTag -> {});
        System.out.println("Suscriptor 2 escuchando mensajes");
    }
}
