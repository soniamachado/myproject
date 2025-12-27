const object = {
  chave1: "valo1",
  chave2: 5,
  chave3: "valor3",
  chave4: [5, 97],
  chave5: {
    "endereco ro": "lisboa",
    novaChave: 5,
  },
};

//que vai ser a mesma chave 3
//const valorChave3 = object.chave3;
//console.log(valorChave3);
//console.log(object["chave3"]); //console.log(object.chave3)

//const { valorChave3 } = object; //estou pegando a chave com o nome "calorChave3" dentro do objeto chamdo "object"
// neste momento não vai dar nada porque valorChave3 não está definida e a forma certa de destruturar:
// const { chave3 } = object; //e assim eu desestruturo as chaves quantas eu quiser:
const { chave1, chave2, chave3 } = object; //e assim eu desestruturo as chaves quantas eu quiser:
console.log(chave1);

//tbm é possível desestruturar array
const array = [5, 25, "text1", "text2", [5, 97]];
//qubrando o array em outras variáveis
const [valor1, valor2, valor3, valor4, valor5] = array;
console.log(valor5);
