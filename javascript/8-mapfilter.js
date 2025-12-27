//map e filter usado para falar em arrays
const array = [5, 25, "texto1", "texto2", [5, 97]];
//Iterar o meu array
//MAP - Vai percorrer cada um dos meus items e vai retornar um novo array do mesmo  tamanho, fazendo algum tipo de modificação para cada item 49min
const array2 = array.map((elementoAtual) => elementoAtual + "Diego");
//=> arrow fucntio para não estar com o return
console.log(array2);
//resposta [ '5Diego', '25Diego', 'texto1Diego', 'texto2Diego', '5,97Diego' ]
const array3 = array.map((elementoAtual) => {});
console.log(array3);
//[ undefined, undefined, undefined, undefined, undefined ]
const array4 = array.map((elementoAtual) => elementoAtual); //gerar um novo array com a regra map num array
console.log(array4);

//FILTER-filtra um array com base em uma condição e retorna um array apenas com os elementos
//que respeitarem a condição do filtro //vai pegar no array e apenas vai usar os elementos que respeitarem aquele filtro

//filtrar tudo que for um número, percorendo cada elemento filter((elementoAtual))
//a mesma coisa que~
const array6 = array.filter((e) => typeof e === "number" && !Number.isNaN(e)); //assim só vai filtrar cuja a filtração for verdadeira, vai retornar apenas os números e excluir isNaN um numero especial, mas não é um número de verdade
console.log(
  "filtra os elementos do array",
  { array },
  "como eu tinha definido em numbers:",
  { array6 }
);
const array7 = array.filter((elementoAtual) => typeof array === "number"); //assim só vai filtrar cuja a filtração for verdadeira
console.log(
  "filtra os elementos do array",
  { array },
  "como eu tinha definido em numbers:",
  { array7 }
);

const array8 = array.filter((elementoAtual) => typeof array !== "number"); //assim só vai filtrar cuja a filtração for verdadeira
console.log(
  "filtra os elementos do array",
  { array },
  "como eu tinha definido em numbers:",
  { array8 }
); //56min fim
