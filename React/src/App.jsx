/*import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'*/ //APAGAR

import ItemLista from "./ItemLista";
import { useState } from "react";
//na verdade para usar sobre o estado é preciso que se tenha variaveis de estado, o react assim renderiza os componentes quando algumas regras acontecerem
// assim que houver alteração na variável de estado todas as partes do componente que dependem dessa variável são atualizadas automaticamente na interface do utilizador
//se eu tenho uma variável sobre o hook useState, quando eu alterar o valor dessa variável, o react vai renderizar o componente novamente
function App() {
  const [ListaMercado, setListaMercado] = useState([]);
  const inputAdicionar = userRe();
  //console.log("Olá mundo!");
  //const [count, setCount] = useState(0) //apagar
  //Hook para guardar o estado da minha lista de mercado
  //array não está armazenar o array, variável de referencia, não é de valor, o endereço do array onde está situada
  //1ºhook a usar useState - cria uma variável de estado
  //ele retorna uma informação
  //ele retorna um array [a variável que armazena a informação, uma função para alterar essa variável]
  const adicionarElementoNaLista = () => {
    const novaLista = [...ListaMercado]; //cópia da lista
    const valorInput = inputAdicionar.current.value;

    //truthy & Falsy
    //'', undefined, null, 0, NaN, false -> Falsy
    //'alguma informação', 123,[], {} -> True
    if (valorInput ) {
    }
    novaLista.push(valorInput); //adicionar um novo item na cópia da lista
    setListaMercado(novaLista);
    inputAdicionar.current.value = "";
    //console.log(novaLista);
    //alterar o estado da minha lista de mercado
    //
    ListaMercado.push("Novo Item"); //adicionar um novo item na cópia da lista
  };
  return (
    <>
      <h1>Lista de Mercado</h1>
      <inputAdicionar.current
        ref={inputAdicionar}
        type="text"
        placeholder="Digit um item"
      />
      <button onClick={() => adicionarElementoNaLista()}>Adicionar</button>
      {/*chamar o componente itemLista */}
      {ListaMercado.length > 0 ? (
        <ul>
          {ListaMercado.map((itemlista, index) => (
            <ItemLista
              key={index}
              itemLista={itemlista}
              ListaMercado={ListaMercado}
              setListaMercado={setListaMercado}
            />
            //eu vou usar cada item da minha lista e retornar cada item da lista prop
          ))}
        </ul>
      ) : (
        <p>A lista está vazia</p>
      )}
    </> //return só devolve um elemento e por isso usar depois do return <> ... </>
    //tag vazia em React se chamar "fragment" <></>
  );
}

export default App;
