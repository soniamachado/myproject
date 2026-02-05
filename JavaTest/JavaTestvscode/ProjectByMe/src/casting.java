//transformar um valor de um tipo para outro tip, casting implicito(trasnformação de um tipo para outro, facil tranformar double par int) e casting explicito

public class casting {
  public static void main(String[] args) {
    //implicito
    int idade1=22;
    double idade2=idade1;
    //mas o inveros não é verdade porque o double é maior que inteiro, casting explicito;
    idade1=(int)idade2;
    char letra='a';
    String nome=String.valueOf(letra); //a string não recebe só uma letra, tem de usar a classe valueof para recerber um char
    //agora de string para char
    letra=nome.charAt(0);

    //transformar um inteiro numa string
    String nome1=String.valueOf(idade1);
    //transformar uma string num inteiro, por exemplo ter 22 como string
    idade1=Integer.parseInt(nome1);
    
    String nome2 = "22"; 
    idade1=Integer.parseInt(nome2);

  }
}
