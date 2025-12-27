console.log("Hello, World!");

let nome = "João";
const idade = 25;
var cidade = "São Paulo"; //evitar usar var

console.log("Nome:", nome);
console.log("Idade:", idade);
console.log("Cidade:", cidade);

nome = "Maria";
console.log("Nome atualizado:", nome);
//tipos primitivos
const numero = 42;
const texto = "Olá, Mundo!";
const booleano = true;
const nulo = null;
let indefinido;
const numerodec = 3.14;
console.log(texto);

//tipos de referencia
const lista = [1, 2, 3, 4, 5];
const array = ["maçã", "banana", "laranja", 4, [5, 6, 7]];
const object = {
  chave: "valor1",
  chave2: "valor2",
  numero: 10,
  chave3: [1, 2, 3],
};
const obj = {
  nome: "João",
  idade: 30,
  endereco: {
    rua: "Rua A",
    cidade: "São Paulo",
  },
};
console.log(array[0]);
console.log(object);
console.log(object.chave3);//console.log(object.[chave3]);

const array2=array
array2[0]=25 //como se trata de uma referencia o array, foi buscar o array e alterar o indice 0

function sum(a, b) {
  return a + b;
}

sum(5, "10");

const a = [1, 2];
const b = a;
b = [2, 3];
///
function add1(array) {
  array = [1, 2, 10];
  console.log(array);
}

let nArray = [1, 2];
add1(nArray);
console.log(nArray);
///
function add10(array) {
  array.push(10);
  console.log(array);
}

let numbersArray = [1, 2];
add10(numbersArray);
console.log(numbersArray);
///
function changeName(n) {
  n = "Carlos";
  console.log(n);
}
