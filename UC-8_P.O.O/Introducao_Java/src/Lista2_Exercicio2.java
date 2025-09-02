public class Exercicio2 {
    public static void main(String[] args) {
        int count = 0;
        int numero = 1;
        
        while (count < 5) {
            if (numero % 2 != 0) {
                System.out.println(numero);
                count++;
            }
            numero++;
        }
    }
}