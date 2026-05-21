import datos.ConexionRabbit;
import presentacion.VentanaSuscriptor;

public class Main {
    public static void main(String[] args) {
        try {
            VentanaSuscriptor ventana = new VentanaSuscriptor();
            ConexionRabbit rabbit = new ConexionRabbit();
            rabbit.conectarYEscuchar(ventana);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
