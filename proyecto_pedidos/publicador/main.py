import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from publicador.presentacion.ventana import VentanaPublicador

if __name__ == "__main__":
    app = VentanaPublicador()
    app.iniciar()
