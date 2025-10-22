import java.util.Scanner;

public class ExibeNumeros {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Este programa exibe todos os números de 1 até o numero escolhido");
        
        System.out.print("Digite um número inteiro: ");
        int numero = scanner.nextInt();
        
        for (int i = 0; i < numero; i++) {
            System.out.println(i + 1);
        }
        
        scanner.close();
    }
}