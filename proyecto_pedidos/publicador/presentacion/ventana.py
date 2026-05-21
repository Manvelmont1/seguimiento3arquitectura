import tkinter as tk
from tkinter import messagebox
from publicador.negocio.pedido import Pedido
from publicador.datos.conexion_rabbit import ConexionRabbit

class VentanaPublicador:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Publicador de Pedidos")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        self.rabbit = ConexionRabbit()
        self._construir_ui()
    
    def _construir_ui(self):
        tk.Label(self.root, text="Publicador de Pedidos", 
                font=("Arial", 16, "bold")).pack(pady=10)
        
        frame = tk.Frame(self.root)
        frame.pack(pady=10, padx=20, fill="both")
        
        tk.Label(frame, text="SKU / ID Producto:", font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=5)
        self.sku_entry = tk.Entry(frame, font=("Arial", 11), width=25)
        self.sku_entry.grid(row=0, column=1, pady=5, padx=10)
        
        tk.Label(frame, text="Cantidad:", font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=5)
        self.cantidad_entry = tk.Entry(frame, font=("Arial", 11), width=25)
        self.cantidad_entry.grid(row=1, column=1, pady=5, padx=10)
        
        tk.Label(frame, text="Talla:", font=("Arial", 11)).grid(row=2, column=0, sticky="w", pady=5)
        self.talla_entry = tk.Entry(frame, font=("Arial", 11), width=25)
        self.talla_entry.grid(row=2, column=1, pady=5, padx=10)
        
        tk.Label(frame, text="Color:", font=("Arial", 11)).grid(row=3, column=0, sticky="w", pady=5)
        self.color_entry = tk.Entry(frame, font=("Arial", 11), width=25)
        self.color_entry.grid(row=3, column=1, pady=5, padx=10)
        
        tk.Button(self.root, text="Enviar Pedido", font=("Arial", 12, "bold"),
                 bg="#4CAF50", fg="white", width=20,
                 command=self._enviar).pack(pady=20)
        
        self.estado_label = tk.Label(self.root, text="", font=("Arial", 10))
        self.estado_label.pack()
    
    def _enviar(self):
        pedido = Pedido(
            self.sku_entry.get(),
            self.cantidad_entry.get(),
            self.talla_entry.get(),
            self.color_entry.get()
        )
        
        valido, mensaje = pedido.validar()
        if not valido:
            messagebox.showerror("Error", mensaje)
            return
        
        try:
            self.rabbit.conectar()
            self.rabbit.enviar_mensaje(pedido.a_json())
            self.rabbit.desconectar()
            self.estado_label.config(text="✅ Pedido enviado correctamente!", fg="green")
            self._limpiar()
        except Exception as e:
            messagebox.showerror("Error", f"Error al enviar: {str(e)}")
    
    def _limpiar(self):
        self.sku_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)
        self.talla_entry.delete(0, tk.END)
        self.color_entry.delete(0, tk.END)
    
    def iniciar(self):
        self.root.mainloop()
        