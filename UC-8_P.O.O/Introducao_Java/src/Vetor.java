public class Vetor {
    public static void main(String[]args)
    {
        int num = 4;
        int[] vetor = new int[num];
        vetor[0] = 21;
        vetor[1] = 28;
        vetor[2] = 38;
        vetor[3] = 41;
        for(int i = 0; i< num; i++){
            System.err.println(vetor[i]);
        }
    }
}
