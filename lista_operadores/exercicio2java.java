import java.util.Scanner;

public class TipoDivisao {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Este programa mostra a divisão inteira e a divisão real");
        System.out.print("Digite o primeiro número: ");
        double number1 = scanner.nextDouble();

        System.out.print("Digite o segundo número: ");
        double number2 = scanner.nextDouble();
        double divisaoreal = number1 / number2;
        double divisaointeira = (double) ((int) (number1 / number2));

        double diferenca = divisaoreal - divisaointeira;
        System.out.println("Divisão real: " + divisaoreal);
        System.out.println("Divisao inteira: " + divisaointeira);
        System.out.println("Diferença entre os resultados: " + diferenca);

        scanner.close();
    }
}