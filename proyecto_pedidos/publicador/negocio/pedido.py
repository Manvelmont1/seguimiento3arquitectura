import json

class Pedido:
    def __init__(self, sku, cantidad, talla, color):
        self.sku = sku
        self.cantidad = cantidad
        self.talla = talla
        self.color = color
    
    def validar(self):
        if not self.sku or self.sku.strip() == "":
            return False, "El SKU no puede estar vacio"
        if not self.cantidad or self.cantidad.strip() == "":
            return False, "La cantidad no puede estar vacía"
        try:
            int(self.cantidad)
        except ValueError:
            return False, "La cantidad debe ser un numero"
        if int(self.cantidad) <= 0:
            return False, "La cantidad debe ser mayor a 0"
        if not self.talla or self.talla.strip() == "":
            return False, "La talla no puede estar vacia"
        if not self.color or self.color.strip() == "":
            return False, "El color no puede estar vacio"
        return True, "OK"
    
    def a_json(self):
        return json.dumps({
            "sku": self.sku,
            "cantidad": int(self.cantidad),
            "talla": self.talla,
            "color": self.color
        })
    