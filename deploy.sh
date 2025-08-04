#!/bin/bash

# TrainSmart API - Script de Deploy Local para Produção

echo "🚀 Iniciando deploy de produção..."

# Verificar se arquivo .env.production existe
if [ ! -f .env.production ]; then
    echo "❌ Arquivo .env.production não encontrado!"
    echo "Copie .env.example para .env.production e configure as variáveis"
    exit 1
fi

# Verificar se Docker está rodando
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker não está rodando!"
    exit 1
fi

# Parar containers existentes
echo "🛑 Parando containers existentes..."
docker-compose down

# Fazer backup do banco (se existir)
if [ -f "exercicios.db" ]; then
    echo "💾 Fazendo backup do banco..."
    cp exercicios.db "backup_$(date +%Y%m%d_%H%M%S).db"
fi

# Build da nova imagem
echo "🔨 Construindo nova imagem..."
docker-compose build --no-cache

# Iniciar containers
echo "🚀 Iniciando containers..."
docker-compose up -d

# Aguardar containers subirem
echo "⏳ Aguardando containers..."
sleep 10

# Verificar saúde da aplicação
echo "🏥 Verificando saúde da aplicação..."
if curl -f http://localhost:8000/health > /dev/null 2>&1; then
    echo "✅ Deploy realizado com sucesso!"
    echo "🌐 API disponível em: http://localhost:8000"
    echo "🏥 Health check: http://localhost:8000/health"
else
    echo "❌ Deploy falhou! Verificar logs:"
    docker-compose logs trainsmart-api
    exit 1
fi

# Mostrar logs finais
echo "📋 Logs recentes:"
docker-compose logs --tail=20 trainsmart-api
