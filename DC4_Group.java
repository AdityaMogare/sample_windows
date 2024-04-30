import java.io.IOException;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.MulticastSocket;

public class DC4_Group {
    public static void main(String[] args) {
        try {
            InetAddress group = InetAddress.getByName("239.0.0.1");
            MulticastSocket socket = new MulticastSocket(1234);
            socket.joinGroup(group);

            Thread receiverThread = new Thread(() -> {
                try {
                    byte[] buffer = new byte[1024];
                    DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
                    while (true) {
                        socket.receive(packet);
                        String message = new String(packet.getData(), 0, packet.getLength());
                        System.out.println("Received: " + message);
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            });
            receiverThread.start();

            while (true) {
                String message = "Hello from sender";
                DatagramPacket packet = new DatagramPacket(message.getBytes(), message.length(), group, 1234);
                socket.send(packet);
                Thread.sleep(1000); // Send message every second
            }

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}