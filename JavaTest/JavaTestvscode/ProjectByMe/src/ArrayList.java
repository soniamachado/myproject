import java.util.ArrayList; 

public class ArrayList {
  public static void main(String[] args) {
  //colocar o array a ser dinâmico poder aumentar o tamanho da lista com outro comando, é um classe de uma lista dinâmica
    ArrayList<Integer> idades=new ArrayList<Integer>();//não determinei qual é o tamanho
    idades.add(22);
    idades.add(58);
    idades.add(30);
    idades.remove(0);//indice é 1
    idades.get(1);//indice é 1, retorna o valor armazenado no indice indicado
    idades.size();//tamanho do array
    idades.clear(2);
  }
}
