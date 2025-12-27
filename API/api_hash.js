/* regras para estruturar as principais metódos HTTP :get, post, put/patch, delete 

GET - pegar dados
POST - criar dados
PUT - atualizar dados
DELETE - deletar dados */
//criar um package para definir já na nossa pasta o node js, e vai criar automaticamente o arquivo package.json nesta pasta, pq assim quando correr vai buscar primeiros os requisitos desta página.

/*1º passo: npm init -y (cria o package.json com as configurações padrão)
2º passo: npm i express (i-instala o express, que é um framework web para node js)como o package.json
 ainda não tem nhenhuma dependência instalada,
 então vamos instalar o express para criar a nossa API

 criou um package-lock.json( arquivo que registra as versões exatas das dependências instaladas no projeto, 
garantindo que todas as instalações futuras usem as mesmas versões, o que ajuda a evitar problemas de compatibilidade)
(é gerado automaticamente pelo npm quando instalamos pacotes)
(não devemos editar manualmente este arquivo, pois ele é gerenciado pelo npm)
modules (pasta onde ficam todas as dependências instaladas no projeto)
3º passo: criar o arquivo api.js (onde vamos criar a nossa API)
arquivo que vai representar a nossa API,
no package.json alterar o type para module (para usar import/export) 


4º passo: node api.js (para correr a nossa API)*/
import express from "express"; //na pasta express dentro do node_modules criado automaticamente quando instalamos o express, retiro a funcao express
const app = express(); //buscar a funcao express para dentro de uma variavel app
//criar uma ligação na porta 3000 do localhost (computador local), e de lado do 3000 dá-se uma função de callback quando a função está a ser chamada
const PORT = 3000;
const arrayResponse = [
  {
    nome: "Minha API",
    versão: "1.0.0",
    descrição: "Esta é a minha primeira API com Express.js",
  },
  { name: "a1", company: "b1" },
  { name: "a2", company: "b2" },
];

//definir uma rota (endereço) para a nossa API;
//tratar das rotas/endpoints padrão e função de resposta, colocar no browser localhost:3000/myproject, tentou pedir um requisito obter a página
//chamar com get, 1ºargumento é o endereço(rota a home, /) trata-se do requisitado, 2º argumento é a função de callback que vai ser executada quando alguém tentar aceder a este endereço (resposta), responder de forma mais simples
app.get("/", (req, res) => {
  res.send("Olá, esta é a minha API com Express!");
}); //não acontece nada se não colocar a correr na linha de comandos node ./api.js
//entrega em JSON-JavaScript Object Notation (formato leve de troca de dados, fácil para humanos lerem e escreverem, e fácil para máquinas analisarem e gerarem) um objeto com informações
/*responder de uma outra forma, só que não posso colocar em json e sent, tenho de colocar  tudo em json

app.get("/", (req, res) => {
  res.json({
    mensagem: "Olá, esta é a minha API com Express!",
    dados: arrResponse
  });
});
------pelo youtber
app.get("/", (req, res) => {
  res.json(arrResponse);
});
*/
//com alteração tenho de reiniciar o servidor (parar e voltar a correr o node api.js) para ver as alterações
//para evitar ter de reiniciar o servidor cada vez que faço uma alteração, instalar o nodemon (ferramenta que reinicia automaticamente o servidor quando detecta alterações no código-fonte)
/*5º passo: npm i -D nodemon (-D instala como dependência de desenvolvimento, ou seja, só é necessário durante o desenvolvimento do projeto, não em produção)
6º passo: no package.json, em scripts, adicionar "start": "nodemon api.js" (para correr o nodemon com o comando npm start)
7º passo: npm start (para correr a nossa API com nodemon)*/
//definir uma rota (endereço) para a nossa API;
//ou cml node --watch ./api.js (para correr a nossa API com reinício automático ao detectar alterações)

app.listen(PORT, () => console.log("Servidor corre na porta", { PORT }));
//definir uma rota (endereço) para a nossa API;
