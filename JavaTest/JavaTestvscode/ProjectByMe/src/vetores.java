public class vetores {
  public static void main(String[] args) {
    int[] idades={2,3,4};
    idades[0] =4;
    System.out.println(idades.length); 
    int[] idade=new int[10];//indicar o tamanho do array, iniciar vazio, e coloco os valores dentro
    System.out.println(idade.length);
    //usar arrays
    String[] nomes= new String[10];//10 nomes
    nomes[1]="rodrigo";
    boolean[] saoPortugueses = {true,false,true}
    ;System.out.println(saoPortugueses.length);
    //coloar um 5 valor no array dos boolean
    //erro atribuir valor que está fora do que foi estipulado neste caso 3 indices x saoPortugueses[5]=false
  }
}
