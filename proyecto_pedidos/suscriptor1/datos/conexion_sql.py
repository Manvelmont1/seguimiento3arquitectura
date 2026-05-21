import pyodbc

class ConexionSQL:
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def conectar(self):
        self.connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=LAPTOP-SQRL55HD\\SQLEXPRESS;"
            "DATABASE=PedidosDB;"
            "UID=sa;"
            "PWD=Solin1227;"
            "TrustServerCertificate=yes;"
        )
        self.cursor = self.connection.cursor()
        return True
    
    def guardar_pedido(self, sku, cantidad, talla, color):
        query = """
            INSERT INTO Pedidos (sku, cantidad, talla, color)
            VALUES (?, ?, ?, ?)
        """
        self.cursor.execute(query, (sku, cantidad, talla, color))
        self.connection.commit()
        return True
    
    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
