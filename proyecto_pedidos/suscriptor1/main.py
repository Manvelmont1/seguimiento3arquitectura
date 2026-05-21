import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from suscriptor1.datos.conexion_rabbit import ConexionRabbit
from suscriptor1.datos.conexion_sql import ConexionSQL
from suscriptor1.negocio.pedido import Pedido

def procesar_mensaje(ch, method, properties, body):
    try:
        mensaje = body.decode("utf-8")
        print(f"📨 Mensaje recibido: {mensaje}")
        
        pedido = Pedido.desde_json(mensaje)
        
        sql = ConexionSQL()
        sql.conectar()
        sql.guardar_pedido(
            pedido.sku,
            pedido.cantidad,
            pedido.talla,
            pedido.color
        )
        sql.desconectar()
        
        print(f"✅ Pedido guardado en SQL Server - SKU: {pedido.sku}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        
    except Exception as e:
        print(f"❌ Error procesando mensaje: {str(e)}")
        ch.basic_nack(delivery_tag=method.delivery_tag)

if __name__ == "__main__":
    rabbit = ConexionRabbit()
    rabbit.conectar()
    rabbit.escuchar(procesar_mensaje)
