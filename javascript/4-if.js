//estrtura if é a estrutura classica de comparação
//se é verdadeiro ou falso no condition if (condition){}
//==comparação não estrita=estou comparando valores
// === comparação estrita= e estou comprando valores e tipos
if (5 == 5) {
  console.log("sim, é igual");
} else {
  console.log("não, é diferente!");
}
//resultado 5= sim, é igual

if (5 == "5") {
  console.log("sim, é igual");
} else {
  console.log("não, é diferente!");
}
//resposta vai ser sim, é igual, porque estou a comparar valores
if (5 === "5") {
  console.log("sim, é igual");
} else {
  console.log("não, é diferente!");
}
//resposta não, é diferente, porque 5 é numero e '5' é uma string
if (5 === "5") {
  console.log("sim, é igual");
} else if (5 === "5") {
  console.log("sim, é igual sem comparar os tipos");
} else {
  console.log("não, é diferente!");
}

if (5 === "5") {
  console.log("sim, é igual");
} else if (5 === "5") {
  console.log("sim, é igual sem comparar os tipos");
} else {
  console.log("não, é diferente!");
}

//OPERADOR TERNÁRIO :forma mais  efeiciente de escrever um if
//usar o operador ternário só para uma única linha
5 === "5" ? console.log("sim, é igual") : console.log("não, é diferente!");
5 == "5" ? console.log("sim, é igual") : console.log("não, é diferente!");
//condição então ?  e os : se o valor for falsa a comparação

const numero = 7;

if (numero > 0 && numero < 10) {
  console.log("Número entre 1 e 9");
}

if (numero === 0 || numero === 10) {
  console.log("Número especial");
}
//operador lógico AND &&  e operador lógico OR ||

//FOR for (inicio; condição; incremento) {
// código
//}
for (let i = 0; i <= 10; i++) {
  console.log(i);
}
//estrutura de repetição for. resposta 0 a  10 cada linha

const array = [5, 25, "texto"];

for (let i = 0; i < array.length; i++) {
  console.log(array[i]);
}

//exemplo de for para iterar um array e mostrar cada elemento do array for+if+and e or
const valore = [5, 10, "ola", 20, null];

for (let i = 0; i < valore.length; i++) {
  if (typeof valore[i] === "number" && !Number.isNaN(valore[i])) {
    console.log("Número válido:", valore[i]);
  }
}
//exemplo de or dentro de um for
const valores = [5, "ola", 0, null];

for (let i = 0; i < valores.length; i++) {
  if (valores[i] === null || valores[i] === 0) {
    console.log("Valor especial:", valores[i]);
  }
}
