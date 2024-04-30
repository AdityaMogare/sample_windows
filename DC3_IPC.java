class SharedData {
    private String message;

    public synchronized String getMessage() {
        return message;
    }

    public synchronized void setMessage(String message) {
        this.message = message;
    }
}

public class DC3_IPC {

    public static void main(String[] args) {
        SharedData sharedData = new SharedData();

        // Create a producer thread (writer)
        Thread producerThread = new Thread(() -> {
            sharedData.setMessage("Hello from the producer!");
        });

        // Create a consumer thread (reader)
        Thread consumerThread = new Thread(() -> {
            String message = sharedData.getMessage();
            System.out.println("Consumer received: " + message);
        });

        producerThread.start();
        consumerThread.start();
        try {
            producerThread.join();
            consumerThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}