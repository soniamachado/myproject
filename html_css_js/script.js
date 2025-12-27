console.log("olá, mundo!");
//document.querySelector("body").innerHTML='<a href="https://www.example.com">Example</a>';
//document.querySelector("body").textContent="sobre mim" (mensagem que vai aparecer na pagina);
//document.querySelectorAll(".sobre").textContent="sobre mim"; não vai funcionar pq o querySelectorAll devolve uma lista de elementos e não um elemento só, estou a dizer que quero mexer no textContent de uma lista de elementos. Tenho de informar qual o elemento da lista que quero alterar, por exemplo o primeiro elemento da lista (índice 0):
//document.querySelectorAll(".sobre")[0].textContent="sobre mim"; //agora sim vai funcionar

//conceito de variável
const elemTexto = document.querySelector(".sobre");
//vantagens usar várias vezes, texto menor; pesquisa mais rápida, porque não preciso de fazer sempre a pesquisa; se quiser mudar a class sobre para função +e automático para outros
const elemInformacoes = document.querySelector(".informacoes");
const elemBotaoInformacoes = document.querySelector(".botao-informacoes");
//elemTexto.textContent = "Sobre mim:";
const elemBotaoDark = document.querySelector(".botao-dark");
const elemBotaoLight = document.querySelector(".botao-light");

//INLINE STYLE
//document.querySelector(".sobre").style.color = "yellow"; //alterou um inline style, mudar a cor das letras

//ADICIONANDO e REMOVENDO classes com add, remove e toogle
elemTexto.classList.add("amarelo");
//para remover o amarelo porque tem lá as duas classes sobre e amarelo: document.querySelector(".sobre").classList.remove("amarelo");
//tbm existe o toggle que permite estar on e off, verifica se no momento estiver on tira a cor, se estiver off coloca a cor, document.querySelector(".sobre").classList.remove("amarelo");
function alterarClasse() {
  console.log("você clicou no texto sobre mim");
  //alert("você clicpu no texto sobre mim");
  //elemTexto.classList.toggle("amarelo");
  elemTexto.classList.toggle("vermelho");
  elemTexto.textContent = "Sobre mim(clicado)";
} // click o que quero monitorirar, que é uma função, significado: tudo vai ser executado quando alguém clicar no elemento a baixo(elemTexto) e estou adicionando um evento nele, um eveneto de click, por isso quando clicar nesse elemento ele vai executar a função, que é definida por uma sequência de ações. estou a remover a classe amarela e colocar a vermelha

//Eventos
elemTexto.addEventListener("click", alterarClasse);
// ou elemTexto.addEventListener("click",function(){alterarClasse)});

//Adicionar o evento de clique no botão do rodapé
elemBotaoInformacoes.addEventListener("click", function () {
  console.log("clique no botão de informações");
  elemInformacoes.classList.toggle("visivel");
  console.log(elemInformacoes.classList.contains("visivel"));
  if (elemInformacoes.classList.contains("visivel")) {
    elemBotaoInformacoes.textContent = "Ocultar informações";
  } else {
    elemBotaoInformacoes.textContent = "Exibir informações";
  }
});
//console.log(elemInformacoes.classList.contains('visivel')); indica se é verdade ou mentira

//Adicionar evento de clique nos botões Ligth/Dark
elemBotaoLight.addEventListener("click", function () {
  console.log("clicou no botão Light");
  document.body.classList.add("ligth");
});

elemBotaoDark.addEventListener("click", function () {
  console.log("clicou no botão Dark");
  document.body.classList.remove("ligth");
});
