import React from "react";
//props vem do meu itemLista no App.jsx
const ItemLista = ({ ItemLista, ListaMercado, setListaMercado }) => {
  //console.log(props.itemLista);
  const removerItemDaLista = () => {
    const novaLista = [...ListaMercado]; //cópia da lista
    const novaListaFiltrada = novaLista.filter(
      (itemAtual) => itemAtual !== ItemLista
    );
    setListaMercado(novaListaFiltrada);
  };
  return (
    <li>
      <p>{ItemLista}</p>
      <button onClick={() => removerItemDaLista()}>Remover</button>
    </li>
  );
};

export default ItemLista;
