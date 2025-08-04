# 🏋️ TrainSmart API

Uma API RESTful completa para gerenciamento de exercícios físicos com sistema de autenticação JWT e controle de acesso baseado em roles.

## 🌐 **API em Produção**
**Base URL:** `https://trainsmart-api.onrender.com`

## 📋 **Índice**
- [Características](#características)
- [Autenticação](#autenticação)
- [Endpoints](#endpoints)
- [Exemplos de Uso](#exemplos-de-uso)
- [Instalação Local](#instalação-local)
- [Deploy](#deploy)

## ✨ **Características**

- 🔐 **Autenticação JWT** com tokens seguros
- 👥 **Sistema de Roles** (Admin/Público)
- 💪 **20 exercícios** pré-populados
- 🔍 **Filtros avançados** por grupo muscular e equipamento
- 🛡️ **Headers de segurança** (CORS, XSS, CSRF)
- 📊 **Health checks** para monitoramento
- 🐳 **Docker** ready
- 🌐 **Deploy** em produção

## 🔐 **Autenticação**

### **Login**
```http
POST /auth/login
Content-Type: application/json

{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

**Resposta:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

> **⚠️ Nota:** Para obter credenciais de acesso, entre em contato com o administrador do sistema.

### **Uso do Token**
```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

## 🎯 **Endpoints**

### **📊 Status e Informações**

#### `GET /` - Informações da API
```http
GET https://trainsmart-api.onrender.com/
```

#### `GET /health` - Health Check
```http
GET https://trainsmart-api.onrender.com/health
```

### **🔐 Autenticação**

#### `POST /auth/login` - Fazer Login
```http
POST https://trainsmart-api.onrender.com/auth/login
Content-Type: application/json

{
  "username": "string",
  "password": "string"
}
```

#### `POST /auth/register` - Registrar Usuário
```http
POST https://trainsmart-api.onrender.com/auth/register
Content-Type: application/json

{
  "username": "string",
  "email": "user@example.com",
  "password": "string"
}
```
> **⚠️ Nota:** Registro bloqueado em produção por segurança

### **💪 Exercícios**

#### `GET /exercicios` - Listar Exercícios (Público)
```http
GET https://trainsmart-api.onrender.com/exercicios
```

**Parâmetros de Query:**
- `grupo_muscular` - Filtrar por grupo muscular
- `equipamento` - Filtrar por equipamento
- `skip` - Pular registros (paginação)
- `limit` - Limitar resultados (máximo 100)

**Exemplo:**
```http
GET https://trainsmart-api.onrender.com/exercicios?grupo_muscular=Peito&limit=5
```

#### `POST /exercicios` - Criar Exercício (Admin)
```http
POST https://trainsmart-api.onrender.com/exercicios
Authorization: Bearer <token>
Content-Type: application/json

{
  "nome": "Supino Reto",
  "descricao": "Exercício para peitorais",
  "grupo_muscular": "Peito",
  "equipamento": "Barra",
  "nivel": "Iniciante",
  "gif_url": "https://example.com/gif.gif"
}
```

#### `GET /exercicios/{id}` - Buscar Exercício por ID
```http
GET https://trainsmart-api.onrender.com/exercicios/1
```

#### `PUT /exercicios/{id}` - Atualizar Exercício (Admin)
```http
PUT https://trainsmart-api.onrender.com/exercicios/1
Authorization: Bearer <token>
Content-Type: application/json

{
  "nome": "Supino Inclinado",
  "descricao": "Exercício para parte superior do peito"
}
```

#### `DELETE /exercicios/{id}` - Excluir Exercício (Admin)
```http
DELETE https://trainsmart-api.onrender.com/exercicios/1
Authorization: Bearer <token>
```

### **📋 Utilitários**

#### `GET /exercicios/grupos-musculares` - Listar Grupos Musculares
```http
GET https://trainsmart-api.onrender.com/exercicios/grupos-musculares
```

#### `GET /exercicios/equipamentos` - Listar Equipamentos
```http
GET https://trainsmart-api.onrender.com/exercicios/equipamentos
```

## 🚀 **Exemplos de Uso**

### **1. Listar todos os exercícios**
```bash
curl https://trainsmart-api.onrender.com/exercicios
```

### **2. Filtrar exercícios de peito**
```bash
curl "https://trainsmart-api.onrender.com/exercicios?grupo_muscular=Peito"
```

### **3. Fazer login e obter token**
```bash
curl -X POST https://trainsmart-api.onrender.com/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"seu_usuario","password":"sua_senha"}'
```

### **4. Criar novo exercício (com token)**
```bash
curl -X POST https://trainsmart-api.onrender.com/exercicios \
  -H "Authorization: Bearer <SEU_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Flexão de Braço",
    "descricao": "Exercício básico para peitorais",
    "grupo_muscular": "Peito",
    "equipamento": "Peso Corporal",
    "nivel": "Iniciante"
  }'
```

## 🔧 **Instalação Local**

### **Pré-requisitos**
- Python 3.11+
- Git

### **1. Clonar Repositório**
```bash
git clone https://github.com/clodomilson-silva/trainsmart-api.git
cd trainsmart-api
```

### **2. Instalar Dependências**
```bash
pip install -r requirements.txt
```

### **3. Configurar Ambiente**
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

### **4. Inicializar Banco de Dados**
```bash
python scripts/criar_admin.py
python scripts/popular_exercicios.py
```

### **5. Executar API**
```bash
python -m uvicorn app.main:app --reload
```

A API estará disponível em: `http://localhost:8000`

## 🐳 **Deploy com Docker**

### **1. Build da Imagem**
```bash
docker-compose build
```

### **2. Executar Container**
```bash
docker-compose up -d
```

## 📊 **Estrutura de Dados**

### **Exercício**
```json
{
  "id": 1,
  "nome": "Supino Reto",
  "descricao": "Exercício para desenvolvimento dos músculos peitorais",
  "grupo_muscular": "Peito",
  "equipamento": "Barra",
  "nivel": "Iniciante",
  "gif_url": "https://example.com/supino-reto.gif"
}
```

### **Usuário**
```json
{
  "id": 1,
  "username": "exemplo_usuario",
  "email": "usuario@exemplo.com",
  "is_admin": false
}
```

## 🔒 **Segurança**

### **⚠️ IMPORTANTE - CREDENCIAIS DE ACESSO**
- **NÃO** compartilhe credenciais de admin publicamente
- **NÃO** inclua senhas reais em documentação
- **USE** variáveis de ambiente para dados sensíveis
- **CONTATE** o administrador para obter acesso

### **🛡️ Medidas de Segurança Implementadas**

- ✅ **JWT Tokens** com expiração
- ✅ **Hashing bcrypt** para senhas
- ✅ **Headers de segurança** (XSS, CSRF, etc.)
- ✅ **CORS** configurado
- ✅ **Rate limiting** (planejado)
- ✅ **HTTPS** obrigatório em produção

## 📝 **Status Codes**

| Código | Descrição |
|--------|-----------|
| 200 | Sucesso |
| 201 | Criado |
| 400 | Requisição inválida |
| 401 | Não autorizado |
| 403 | Proibido |
| 404 | Não encontrado |
| 422 | Erro de validação |
| 500 | Erro interno |

## 🤝 **Contribuindo**

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Add: nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 **Licença**

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 **Autor**

**Clodomilson Silva**
- GitHub: [@clodomilson-silva](https://github.com/clodomilson-silva)
- Email: clodomilsonanjos.eng@outlook.com

---

⭐ **Se este projeto te ajudou, deixe uma estrela!**
