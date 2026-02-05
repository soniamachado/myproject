# syntax=docker/dockerfile:1

FROM node:lts-alpine
#imagem pai
WORKDIR /app
COPY . .
#em cima estamos a dizer que vamos copiar tudo o que esta na pasta atual para a pasta /app dentro do container
RUN yarn install --production
#instalado os pacotes de produção por meio do yarn
CMD ["node", "src/index.js"]
#qual o comando a ser executado quando o container iniciar
EXPOSE 3000
#porta a ser exposta do container