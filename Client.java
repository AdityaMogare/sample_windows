import java.rmi.Naming;

public class Client {

    public static void main(String[] args) throws Exception {
        Adder1 stub = (Adder1) Naming.lookup("rmi://localhost:5001/sunoo");

        int sum = stub.add(6, 2);

        System.out.println("The sum is: " + sum);
    }
}
