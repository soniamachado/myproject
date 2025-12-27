//nada mais que funções escritas de outra forma
//video https://www.youtube.com/watch?v=pBcGYStGLUo&t=258s 38min
const consoleLogOi = (parametro1, parametro2) => {
  console.log(parametro1);
  return parametro2;
};
//exemplo de chamada da função
consoleLogOi("oi", "tudo bem?");
//arrow function com retorno implícito
const soma = (a, b) => a + b;
//chamada da função soma
console.log(soma(2, 3));
//arrow function com um unico parametro (não precisa de parenteses)
const quadrado = (x) => x * x;
//chamada da função quadrado
console.log(quadrado(4));
//arrow function sem parametros (precisa dos parenteses)
//foi criada arrow function de modo a retornar outra função, por isso o return

//outra função que não recebe nenhum parametro e vai executar 'segunda função'
const segundaFuncao = () => console.log("segunda função");
//para executar segundaFuncao()
const retornoDaFuncao = consoleLogOi();
console.log(retornoDaFuncao);

//código curto e legivel
function soma(a, b) {
  return a + b;
}
console.log(soma(2, 3));

const somaArrow = (a, b) => a + b;
console.log(somaArrow(2, 3));
const funcaoSemParametro = () => console.log("função sem parametro");
funcaoSemParametro();

//Perfeitas para callbacks (map, filter, forEach), ANTES
array.filter(function (n) {
  return n > 10;
});
//DEPOIS
array.filter((n) => n > 10);
//outras formas
array.filter((n) => {
  return n > 10;
});
