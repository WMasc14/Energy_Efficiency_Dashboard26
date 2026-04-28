# Use imagem Python oficial
FROM python:3.11-slim

WORKDIR /app

# Instalar Node.js (para build do frontend)
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Copiar arquivos do projeto
COPY package*.json ./
COPY requirements.txt ./

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Instalar dependências Node.js
RUN npm install --legacy-peer-deps

# Copiar código
COPY . .

# Build do frontend
RUN npm run build

# Expor portas
EXPOSE 8000 3000

# Comando de inicialização
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
