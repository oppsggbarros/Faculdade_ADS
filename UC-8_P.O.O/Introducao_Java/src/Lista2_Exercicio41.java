public class Exercicio41 {
    public static void main(String[] args) {
        long soma = 0;
        long somaQuadrados = 0;
        
        for (int i = 1; i <= 100; i++) {
            soma += i;
            somaQuadrados += i * i;
        }
        
        long quadradoSoma = soma * soma;
        long diferenca = quadradoSoma - somaQuadrados;
        
        System.out.println("Soma dos quadrados: " + somaQuadrados);
        System.out.println("Quadrado da soma: " + quadradoSoma);
        System.out.println("Diferença: " + diferenca);
    }
}