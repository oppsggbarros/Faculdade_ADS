public class Exercicio28 {
    public static void main(String[] args) {
        double salario = 4000.0;
        double percentualAumento = 1.5;
        int anoAtual = 2024; // Alterar conforme necessário
        
        for (int ano = 2020; ano <= anoAtual; ano++) {
            salario += salario * (percentualAumento / 100);
            percentualAumento *= 2; // Dobra o percentual para o próximo ano
        }
        
        System.out.printf("Salário em %d: R$ %.2f\n", anoAtual, salario);
    }
}