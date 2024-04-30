import java.rmi.*;
public interface Adder1 extends Remote
{
    public int add(int a ,int b) throws RemoteException;
}
