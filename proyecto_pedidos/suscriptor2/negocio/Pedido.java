package negocio;

public class Pedido {
    private String sku;
    private int cantidad;
    private String talla;
    private String color;

    public Pedido(String sku, int cantidad, String talla, String color) {
        this.sku = sku;
        this.cantidad = cantidad;
        this.talla = talla;
        this.color = color;
    }

    public String getSku() { return sku; }
    public int getCantidad() { return cantidad; }
    public String getTalla() { return talla; }
    public String getColor() { return color; }

    @Override
    public String toString() {
        return "SKU: " + sku + " | Cantidad: " + cantidad + 
               " | Talla: " + talla + " | Color: " + color;
    }
}
