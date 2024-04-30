import java.rmi.*;  

public class ServerName{  
public static void main(String args[]){  
try{  
Adder1 stub=new Server();  
Naming.rebind("rmi://localhost:5001/sunoo",stub);  
}catch(Exception e){System.out.println(e);}  
}  
}  