FROM node:18-alpine

WORKDIR /app

# Copiar arquivos do projeto
COPY . .

# Instalar dependências
RUN npm install

# Expor porta
EXPOSE 10000

# Comando para iniciar
CMD ["npx", "serve", "-s", ".", "-l", "10000"]
