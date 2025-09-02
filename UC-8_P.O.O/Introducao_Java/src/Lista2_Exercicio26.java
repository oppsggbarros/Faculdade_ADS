public class Exercicio26 {
    public static void main(String[] args) {
        double S = 0;
        
        for (int i = 1; i <= 100; i++) {
            S += 1.0 / i;
        }
        
        System.out.println("Valor de S: " + S);
    }
}