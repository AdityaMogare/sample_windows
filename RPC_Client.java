public class Client {
    public static void main(String[] args) {
        RPCClient rpcClient = new RPCClient("server-address", 5001);
        int sum = rpcClient.call("add", 6, 2);
        System.out.println("The sum is: " + sum);
    }
}
