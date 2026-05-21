import json

class Pedido:
    def __init__(self, sku, cantidad, talla, color):
        self.sku = sku
        self.cantidad = cantidad
        self.talla = talla
        self.color = color
    
    @staticmethod
    def desde_json(mensaje):
        datos = json.loads(mensaje)
        return Pedido(
            sku=datos["sku"],
            cantidad=datos["cantidad"],
            talla=datos["talla"],
            color=datos["color"]
        )
