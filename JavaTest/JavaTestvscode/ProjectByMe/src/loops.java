import java.util.Scanner;

public class loops {
  
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("Introduza o tamanho do array: ");
    int tamanho = scanner.nextInt();
    int[] numeros = new int[tamanho]; 
    for(int i=0; i<numeros.length; i++){
       numeros[i] = i*2;
       System.out.print(numeros[i] + " ");}
    int idade=10;
    for (var i=0;i<idade;i++){System.out.println("oi");}
    int altura=10;
    int i=0;
    while (i<altura){
      i++;
    }
  }
}
