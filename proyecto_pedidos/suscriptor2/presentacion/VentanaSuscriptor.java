package presentacion;

import negocio.Pedido;
import javax.swing.*;
import java.awt.*;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class VentanaSuscriptor {
    private JFrame frame;
    private JTextArea textArea;
    private JLabel estadoLabel;

    public VentanaSuscriptor() {
        _construirUI();
    }

    private void _construirUI() {
        frame = new JFrame("Suscriptor 2 - Mensajes RabbitMQ");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);
        frame.setResizable(false);
        frame.setLayout(new BorderLayout());

        JLabel titulo = new JLabel("Mensajes Recibidos", SwingConstants.CENTER);
        titulo.setFont(new Font("Arial", Font.BOLD, 16));
        titulo.setBorder(BorderFactory.createEmptyBorder(10, 0, 10, 0));
        frame.add(titulo, BorderLayout.NORTH);

        textArea = new JTextArea();
        textArea.setFont(new Font("Arial", Font.PLAIN, 12));
        textArea.setEditable(false);
        textArea.setBackground(new Color(245, 245, 245));
        JScrollPane scrollPane = new JScrollPane(textArea);
        scrollPane.setBorder(BorderFactory.createEmptyBorder(5, 10, 5, 10));
        frame.add(scrollPane, BorderLayout.CENTER);

        estadoLabel = new JLabel("✅ Escuchando mensajes...", SwingConstants.CENTER);
        estadoLabel.setFont(new Font("Arial", Font.PLAIN, 11));
        estadoLabel.setForeground(new Color(76, 175, 80));
        estadoLabel.setBorder(BorderFactory.createEmptyBorder(5, 0, 10, 0));
        frame.add(estadoLabel, BorderLayout.SOUTH);

        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

    public void mostrarPedido(Pedido pedido) {
        SwingUtilities.invokeLater(() -> {
            String fecha = LocalDateTime.now()
                .format(DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss"));
            String linea = "[" + fecha + "] " + pedido.toString();
            textArea.append(linea + "\n");
            guardarEnTxt(linea);
        });
    }

    private void guardarEnTxt(String linea) {
        try (FileWriter fw = new FileWriter("pedidos.txt", true)) {
            fw.write(linea + "\n");
        } catch (IOException e) {
            estadoLabel.setText("Error guardando en archivo: " + e.getMessage());
            estadoLabel.setForeground(Color.RED);
        }
    }
}
