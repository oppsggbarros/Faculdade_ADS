import java.util.Scanner;

public class Exercicio44 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int maisVelho = 0;
        double maisAlto = 0;
        double maiorPeso = 0;
        double somaAltura = 0;
        double somaIMC = 0;
        int homens = 0;
        int mulheres = 0;
        
        for (int i = 0; i < 25; i++) {
            System.out.println("\nPessoa " + (i + 1) + ":");
            
            System.out.print("Idade: ");
            int idade = scanner.nextInt();
            
            System.out.print("Sexo (M/F): ");
            char sexo = scanner.next().charAt(0);
            
            System.out.print("Altura (m): ");
            double altura = scanner.nextDouble();
            
            System.out.print("Peso (kg): ");
            double peso = scanner.nextDouble();
            
            // Atualiza estatísticas
            if (idade > maisVelho) maisVelho = idade;
            if (altura > maisAlto) maisAlto = altura;
            if (peso > maiorPeso) maiorPeso = peso;
            
            somaAltura += altura;
            
            double imc = peso / (altura * altura);
            somaIMC += imc;
            
            if (Character.toUpperCase(sexo) == 'M') {
                homens++;
            } else {
                mulheres++;
            }
        }
        
        // Cálculos finais
        double mediaAltura = somaAltura / 25;
        double mediaIMC = somaIMC / 25;
        double percentualHomens = (double) homens / 25 * 100;
        double percentualMulheres = (double) mulheres / 25 * 100;
        
        System.out.println("\n=== ESTATÍSTICAS DA ACADEMIA ===");
        System.out.println("Idade da pessoa mais velha: " + maisVelho);
        System.out.println("Altura da pessoa mais alta: " + maisAlto + "m");
        System.out.println("Maior peso: " + maiorPeso + "kg");
        System.out.printf("Média de altura: %.2fm\n", mediaAltura);
        System.out.printf("Média de IMC: %.2f\n", mediaIMC);
        System.out.printf("Percentual de homens: %.2f%%\n", percentualHomens);
        System.out.printf("Percentual de mulheres: %.2f%%\n", percentualMulheres);
        
        scanner.close();
    }
}