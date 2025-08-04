#!/usr/bin/env bash
# Build script for Render

echo "🔧 Iniciando build para produção..."

# Install dependencies
echo "📦 Instalando dependências..."
pip install -r requirements.txt

echo "🗄️ Configurando banco de dados..."
# Create database and populate with data
python scripts/criar_admin.py
python scripts/popular_exercicios.py

echo "✅ Build concluído com sucesso!"
