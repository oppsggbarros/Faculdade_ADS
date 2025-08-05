import java.util.Scanner;

public class Exercicio41 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Digite os coeficientes da equação ax² + bx + c = 0");
        System.out.print("a: ");
        double a = scanner.nextDouble();
        
        System.out.print("b: ");
        double b = scanner.nextDouble();
        
        System.out.print("c: ");
        double c = scanner.nextDouble();
        
        if (a == 0) {
            System.out.println("Não é equação de segundo grau");
        } else {
            double delta = b * b - 4 * a * c;
            
            if (delta < 0) {
                System.out.println("Não existe raiz real");
            } else if (delta == 0) {
                double raiz = -b / (2 * a);
                System.out.printf("Raiz única: %.2f\n", raiz);
            } else {
                double raiz1 = (-b + Math.sqrt(delta)) / (2 * a);
                double raiz2 = (-b - Math.sqrt(delta)) / (2 * a);
                System.out.printf("Duas raízes reais: %.2f e %.2f\n", raiz1, raiz2);
            }
        }
        
        scanner.close();
    }
}