FROM node:24.13.0-alpine3.22 AS dev
ENV NODE_ENV=development
WORKDIR /app
COPY . .
RUN npm ci
EXPOSE 3000
CMD ["npm","run", "dev"]
#vai ser iniciada a aplicação pelo comando npm run dev,  do container na porta 3000