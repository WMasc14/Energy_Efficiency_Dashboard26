#!/bin/bash
# Script de deploy automático

echo "=== Deploy Automático ReactorLab ==="

# Detectar plataforma
if [ "$1" == "heroku" ]; then
    echo "Deploy para Heroku..."
    heroku login
    heroku create
    git push heroku main
    echo "✓ Deploy concluído em Heroku!"
    
elif [ "$1" == "render" ]; then
    echo "Deploy para Render.com..."
    echo "1. Acesse https://render.com"
    echo "2. Conecte seu repositório GitHub"
    echo "3. Crie novo Web Service"
    echo "4. Build: pip install -r requirements.txt && npm install && npm run build"
    echo "5. Start: uvicorn main:app --host 0.0.0.0 --port \$PORT"
    
elif [ "$1" == "docker" ]; then
    echo "Building Docker..."
    docker build -t reactorlab .
    echo "✓ Docker image criada!"
    echo "Para rodar: docker run -p 8000:8000 reactorlab"
    
else
    echo "Uso: ./deploy.sh [heroku|render|docker]"
    echo ""
    echo "Exemplo:"
    echo "  ./deploy.sh docker"
    echo "  ./deploy.sh heroku"
    echo "  ./deploy.sh render"
fi
