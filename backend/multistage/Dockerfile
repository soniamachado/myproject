#estágio 0 o FROM
FROM ubuntu AS build
RUN apt update && apt install build-essential -y
RUN mkdir /opt/app
WORKDIR /opt/app
COPY Main.c .
# /opt/app/MAIN.c
#com run vamos correr de modo a compilar em binário o arquivo Main.c e gerar o arquivo Main
#com static é dizer que é autosufeciente e que funcionar em qualquer SO linux(alpine, ubuntu, debian), que não precisas de bibliotecas externas em runtime
RUN gcc ./Main.c -static -o Main

#scratch é uma imagem bases minima que trago do linux,o from é o estágio que se quer copiar em cima,que quero copiar o arquivo MAIN que está em /opt/app/Main, e Destino /Main
FROM alpine AS prd
COPY --from=0 /opt/app/Main /opt/app/Main
FROM prd AS run
CMD ["/opt/app/Main"]
#CMD ["/bin/sh", "-c","/opt/app/Main"]