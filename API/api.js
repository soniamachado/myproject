//agora instalado o Node JS, vamos instalar o React (biblioteca JavaScript para construir interfaces de usuário) e o Create React App (ferramenta oficial para criar aplicativos React com configuração zero)
//API application programming interface
//REST -representational State transfer (traduz um conjunto de regras de boas práticas para criação de API escaláveis : principais regras/métodos e requição HTTP)
//métodos principais HTTP: GET, POST, PUT, DELETE

//API RESTful - API que segue as regras do REST
//Métodos HTTP mais usados em API RESTful
//GET - pegar dados
//POST - criar dados
//PUT - atualizar dados
//DELETE - deletar dados
//Exemplo de uma API RESTful de usuários
//GET /users - pegar todos os usuários
//GET /users/1 - pegar o usuário com ID 1
//POST /users - criar um novo usuário
//PUT /users/1 - atualizar o usuário com ID 1
//DELETE /users/1 - deletar o usuário com ID 1
//APIs podem retornar dados em vários formatos, mas o mais comum é JSON (JavaScript Object Notation)
//Exemplo de resposta JSON para GET /users
/*
[
  {
    "id": 1,
    "name": "Diego",
    "email": "diego@hotmail.com"
  },
  {
    "id": 2,
    "name": "Sonia",
    "email": "sonia@hotmail.com"
  }
]
*/
//APIs RESTful são amplamente utilizadas no desenvolvimento web e mobile para permitir a comunicação entre o cliente (frontend) e o servidor (backend)
//Elas são simples, escaláveis e fáceis de entender, tornando-as uma escolha popular para a construção de serviços web.
//Comparação entre JavaScript puro e fetch API para fazer uma requisição GET
//JavaScript puro (XMLHttpRequest)
const xhr = new XMLHttpRequest();
xhr.open("GET", "https://api.exemplo.com/dados");
xhr.onload = function () {
  if (xhr.status === 200) {
    const dados = JSON.parse(xhr.responseText);
    console.log(dados);
  } else {
    console.error("Erro na requisição:", xhr.status);
  }
};
xhr.send();

//fetch API
fetch("https://api.exemplo.com/dados")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Erro na requisição: " + response.status);
    }
    return response.json();
  })
  .then((dados) => {
    console.log(dados);
  })
  .catch((error) => {
    console.error(error);
  });
