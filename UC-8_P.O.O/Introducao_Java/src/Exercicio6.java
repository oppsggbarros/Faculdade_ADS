import java.util.Scanner;

public class Exercicio6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Em qual turno você estuda? (M-Matutino, V-Vespertino, N-Noturno): ");
        char turno = scanner.next().charAt(0);
        
        switch (turno) {
            case 'M':
            case 'm':
                System.out.println("Bom Dia!");
                break;
            case 'V':
            case 'v':
                System.out.println("Boa Tarde!");
                break;
            case 'N':
            case 'n':
                System.out.println("Boa Noite!");
                break;
            default:
                System.out.println("Valor Inválido!");
        }
        
        scanner.close();
    }
}