import java.util.Scanner;
public class App {
    public static void maain(String []args) {
        Scanner sc =new Scanner(System.in);
        int num;
        System.out.println("Número");
        num = sc.nextInt();
        System.out.print(num);
        sc.close();
    }
}