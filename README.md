# 🏋️ TrainSmart API

## 🎯 Sobre o Projeto
API REST completa para exercícios físicos com autenticação JWT e autorização baseada em perfis. Ideal para aplicações de fitness, personal trainers e academias.

## ⚡ Quick Start

### 1. Configuração Inicial
```bash
# Clone ou baixe o projeto
cd trainsmart_api

# Crie ambiente virtual
python -m venv venv

# Ative o ambiente (Windows)
venv\Scripts\activate

# Instale dependências
pip install -r requirements.txt
```

### 2. Configuração do Banco
```bash
# Crie usuário administrador
python scripts/criar_admin.py

# Popular com exercícios (opcional - já tem 20 exercícios)
python scripts/popular_exercicios.py
```

### 3. Executar API
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Acessar Documentação
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 🔑 Credenciais Padrão
- **Username:** admin
- **Password:** admin123
- **Email:** admin@trainsmart.com

## 📋 Endpoints Principais

### 🔓 Públicos (GET apenas)
```
GET /exercicios/                     # Lista exercícios com filtros
GET /exercicios/{id}                 # Detalhes de exercício
GET /exercicios/grupos-musculares    # Lista grupos únicos
GET /exercicios/equipamentos         # Lista equipamentos únicos
```

### 🔐 Administrativos (Requer token)
```
POST   /exercicios/       # Criar exercício
PUT    /exercicios/{id}   # Atualizar exercício
DELETE /exercicios/{id}   # Deletar exercício
```

### 🔑 Autenticação
```
POST /auth/register       # Registrar usuário comum
POST /auth/register-admin # Registrar admin
POST /auth/token         # Login (obter JWT)
```

## 🎛️ Filtros Disponíveis
```
?grupo_muscular=Peito              # Filtrar por grupo
?equipamento=Halteres              # Filtrar por equipamento
?skip=10&limit=20                  # Paginação
?grupo_muscular=Pernas&skip=5      # Múltiplos filtros
```

## 💻 Exemplos de Uso

### Listar exercícios de peito
```bash
curl "http://localhost:8000/exercicios/?grupo_muscular=Peito"
```

### Login de admin
```bash
curl -X POST "http://localhost:8000/auth/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=admin&password=admin123"
```

### Criar exercício (como admin)
```bash
curl -X POST "http://localhost:8000/exercicios/" \
     -H "Authorization: Bearer SEU_TOKEN_AQUI" \
     -H "Content-Type: application/json" \
     -d '{
       "nome": "Novo Exercício",
       "grupo_muscular": "Braços",
       "descricao": "Descrição detalhada",
       "equipamento": "Halteres",
       "gif_url": "https://exemplo.com/exercicio.gif"
     }'
```

## 🏗️ Arquitetura

```
📁 app/
  ├── main.py          # FastAPI app + CORS
  ├── database.py      # SQLAlchemy config
  ├── models.py        # Exercicio + Usuario models
  ├── schemas.py       # Pydantic schemas
  ├── crud.py          # Database operations
  ├── auth.py          # JWT authentication
  ├── utils.py         # Password hashing
  └── routes/
      ├── exercicios.py # Exercise endpoints
      └── auth.py       # Auth endpoints

📁 scripts/
  ├── popular_exercicios.py # Seed database
  ├── criar_admin.py       # Create admin user
  └── test_api.py         # API tests
```

## 🔧 Stack Tecnológica

- **FastAPI** - Framework web moderno
- **SQLAlchemy** - ORM Python
- **JWT** - Autenticação stateless
- **bcrypt** - Hash seguro de senhas
- **Pydantic V2** - Validação de dados
- **SQLite** - Banco de dados (substituível)

## 🛡️ Segurança

### Níveis de Acesso
- **👥 Público:** Apenas leitura (GET)
- **🔐 Admin:** CRUD completo

### Recursos de Segurança
- ✅ Tokens JWT com expiração
- ✅ Senhas hasheadas com bcrypt
- ✅ Autorização baseada em roles
- ✅ CORS configurado
- ✅ Validação de dados

## 📊 Dados Inclusos

- **20 exercícios** populados
- **8 grupos musculares**
- **15 tipos de equipamento**
- **GIFs demonstrativas** funcionais

## 🧪 Testes

```bash
# Executar testes automatizados
python scripts/test_api.py
```

## 🚀 Deploy

### Docker (Recomendado)
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Railway/Heroku
```bash
# Criar Procfile
echo "web: uvicorn app.main:app --host 0.0.0.0 --port \$PORT" > Procfile
```

## 📈 Melhorias Futuras

### 🔧 Técnicas
- [ ] Variáveis de ambiente
- [ ] Rate limiting
- [ ] Logging estruturado
- [ ] Cache Redis
- [ ] PostgreSQL

### 🎯 Funcionais
- [ ] Upload de GIFs
- [ ] Sistema de favoritos
- [ ] Histórico de treinos
- [ ] Recomendações IA
- [ ] Múltiplos idiomas

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch: `git checkout -b feature/nova-funcionalidade`
3. Commit: `git commit -m 'Adiciona nova funcionalidade'`
4. Push: `git push origin feature/nova-funcionalidade`
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja LICENSE para mais detalhes.

## 🆘 Suporte

- **Documentação:** http://localhost:8000/docs
- **Issues:** Abra uma issue no repositório
- **Email:** suporte@trainsmart.com

---

**🎯 Pronto para usar!** Sua API de exercícios está completa e funcionando.
