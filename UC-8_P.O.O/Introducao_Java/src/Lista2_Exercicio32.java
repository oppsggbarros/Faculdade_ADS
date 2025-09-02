import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Exercicio32 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Character> consoantes = new ArrayList<>();
        int totalConsoantes = 0;
        
        System.out.println("Digite 10 caracteres:");
        for (int i = 0; i < 10; i++) {
            System.out.print("Caracter " + (i + 1) + ": ");
            char c = scanner.next().charAt(0);
            
            if (isConsoante(c)) {
                consoantes.add(c);
                totalConsoantes++;
            }
        }
        
        System.out.println("Total de consoantes: " + totalConsoantes);
        System.out.println("Consoantes lidas: " + consoantes);
        scanner.close();
    }
    
    private static boolean isConsoante(char c) {
        c = Character.toLowerCase(c);
        return Character.isLetter(c) && c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u';
    }
}