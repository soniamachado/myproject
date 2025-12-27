const array = [5, 25, "text1", "text2", [5, 97]];

//vou fazer uma copia e quero acrescentar no meu array
const array2 = [...array]; //... pego na informação do meu array e espalho; é outro endereço, e este endereço tem as mesmas informações
//[...array]-trata-se  de um spread operate
// array2[0] = 13513;

console.log(array2);
console.log(array);
//resusltado array2=[13513,25,text1,text2,[5,97]]
//resultado array1[5,25,'text1','texto2',[5,97]]
//o mesmo pode acontecer com chaves
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
export const object2 = { ...object }; //já sabemos que ele está a apanhar este objeto e espalhar
//export, defino que estou a export para que alguém possa importar o objeto
console.log(object2);
