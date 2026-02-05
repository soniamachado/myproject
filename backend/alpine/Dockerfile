ARG ALPINE_VERSION=3.23.2
#ARG não gera camada
FROM alpine:${ALPINE_VERSION}
#instalando dependências no SO

#não gera camada
LABEL desenvolvedor="Bruno Luiz"
ENV HOST="0.0.0.0"
#1 camada
RUN apk add --no-cache
#2 camada ->#1+#2
RUN apk add --no-cache nodejs
#3 camada   ->#2+#3 
RUN apk add --no-cache npm 
#4 camada ->#3+#4
RUN apk add --no-cache git
#5 camada ->#4+#5
RUN apk add --no-cache wget

WORKDIR /opt/
#6 camada->#5+#6
#ENTRYPOINT ["node"] 
#retiar o entrpoint, porque se quer acessar o terminal interatibo do container
#cmd não gera camada
#CMD ["--version"]
