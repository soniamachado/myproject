//no react vamos mexer em vários arquivos, código separados em arquivos diferentes
import { object2 } from "./3-spread.js"; //desestruturação- o from está me retornando um objeto
//com todos os exports daquele arquivo. Como eu só o export 'object2', eu tenho que destruturar.

console.log(object2);
//não vai dar porque estou a usar o javascript cru com ..Export.js por isso é necessário renomear o nome importExport.js
//para 7-importExport.mjs

//outro erro importar do outro ficheiro pd tbm não é um modulo '3-spread.mjs'
//MAS DÁ MUiTo TRABALHO AQUILO QUE QUERO EXPORTAR E AQUILO QUE NÃO QUERO

//na verdade na consola vai-se colocar > npm init -y   //na verdade ele vai iniciar um arquivo do nmp (node packet manager-gerencia os pacotes do node que estão disponiveis para poder instalar, e ele faz um arquivo de ocnfiguração padrão, do tipo package.json)
//npm faz um arquivo de configuração padrão
//e nmp init cria um arquivo padrão

/*
npm init -y
O -y significa “yes para tudo”.

O comando aceita automaticamente todos os valores padrão dessas perguntas (name, version, etc.) sem te perguntar nada.

Cria imediatamente um package.json com as opções default, mais rápido para testes e pequenos projetos.
*/
//criou um ficvheiro  package.json que tem algumas configurações
//cria-se pq quando se tem um projeto pelo caminho vai dizendo todos os pacotes que tenho dentro do projeto
// e dentro do ficheiro package.json com type:module, consigo dizer que todos os arquivos dentro do javascript usam o type"module"
//46min
