import java.util.Scanner;

public class VerificadorLogin {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Este programa verifica seu login");

        System.out.print("Digite seu usuário: ");
        String usuario = scanner.nextLine(); 

        System.out.print("Digite sua senha: ");
        if (scanner.hasNextInt()) {
            int senha = scanner.nextInt();

            if (usuario.equals("admin") && senha == 1234) {
                System.out.println("ACESSO PERMITIDO!");
            } else {
                System.out.println("Acesso negado...tente novamente!");
            }
        } else {
            System.out.println("Acesso negado... A senha deve ser um número inteiro.");
        }
    }
}