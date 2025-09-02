import java.util.Scanner;

public class Exercicio42 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] votos = new int[6]; // índices: 0-3 candidatos, 4 nulos, 5 brancos
        int totalVotos = 0;
        int voto;
        
        System.out.println("Candidatos:");
        System.out.println("1 - José");
        System.out.println("2 - João");
        System.out.println("3 - Maria");
        System.out.println("4 - Ana");
        System.out.println("5 - Voto Nulo");
        System.out.println("6 - Voto em Branco");
        System.out.println("0 - Encerrar votação");
        
        do {
            System.out.print("Digite seu voto: ");
            voto = scanner.nextInt();
            
            if (voto >= 1 && voto <= 6) {
                votos[voto - 1]++;
                totalVotos++;
            } else if (voto != 0) {
                System.out.println("Voto inválido!");
            }
        } while (voto != 0);
        
        System.out.println("\n=== RESULTADOS ===");
        System.out.println("José: " + votos[0] + " votos");
        System.out.println("João: " + votos[1] + " votos");
        System.out.println("Maria: " + votos[2] + " votos");
        System.out.println("Ana: " + votos[3] + " votos");
        System.out.println("Votos nulos: " + votos[4]);
        System.out.println("Votos em branco: " + votos[5]);
        System.out.println("Total de votos: " + totalVotos);
        
        double percentualNulos = (double) votos[4] / totalVotos * 100;
        double percentualBrancos = (double) votos[5] / totalVotos * 100;
        
        System.out.printf("Percentual de nulos: %.2f%%\n", percentualNulos);
        System.out.printf("Percentual de brancos: %.2f%%\n", percentualBrancos);
        scanner.close();
    }
}