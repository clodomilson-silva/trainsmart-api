# TrainSmart API - Documentação

## Visão Geral
API REST para exercícios físicos com autenticação e autorização baseada em perfis de usuário.

## Funcionalidades

### 🔓 Acesso Público (GET apenas)
- **Listar exercícios** com filtros
- **Detalhes de exercícios específicos**
- **Listar grupos musculares únicos**
- **Listar equipamentos únicos**

### 🔐 Acesso de Administrador (CRUD completo)
- **Criar** novos exercícios
- **Atualizar** exercícios existentes  
- **Deletar** exercícios

## Endpoints Principais

### Autenticação
- `POST /auth/register` - Registrar usuário comum
- `POST /auth/register-admin` - Registrar administrador
- `POST /auth/token` - Login e obter token JWT

### Exercícios (Público)
- `GET /exercicios/` - Listar exercícios com filtros opcionais
- `GET /exercicios/{id}` - Detalhes de um exercício
- `GET /exercicios/grupos-musculares` - Lista grupos musculares únicos
- `GET /exercicios/equipamentos` - Lista equipamentos únicos

### Exercícios (Admin apenas)
- `POST /exercicios/` - Criar exercício
- `PUT /exercicios/{id}` - Atualizar exercício
- `DELETE /exercicios/{id}` - Deletar exercício

## Filtros Disponíveis

### Parâmetros de Query
- `grupo_muscular` - Filtrar por grupo muscular (ex: "Peito", "Costas")
- `equipamento` - Filtrar por equipamento (ex: "Halteres", "Peso corporal")
- `skip` - Número de exercícios para pular (paginação)
- `limit` - Limite de exercícios por página (máx: 1000)

### Exemplos de URLs
```
GET /exercicios/?grupo_muscular=Peito
GET /exercicios/?equipamento=Halteres
GET /exercicios/?grupo_muscular=Pernas&equipamento=Peso corporal
GET /exercicios/?skip=10&limit=20
```

## Autenticação

### Login de Administrador Padrão
- **Username:** admin
- **Password:** admin123
- **Email:** admin@trainsmart.com

### Como Autenticar
1. **Login:** `POST /auth/token` com username/password
2. **Token:** Receber JWT token na resposta
3. **Headers:** Incluir `Authorization: Bearer {token}` nas requisições protegidas

### Exemplo de Login
```bash
curl -X POST "http://localhost:8000/auth/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=admin&password=admin123"
```

### Exemplo de Requisição Autenticada
```bash
curl -X POST "http://localhost:8000/exercicios/" \
     -H "Authorization: Bearer {seu_token_jwt}" \
     -H "Content-Type: application/json" \
     -d '{
       "nome": "Novo Exercício",
       "grupo_muscular": "Braços",
       "descricao": "Descrição do exercício",
       "equipamento": "Halteres",
       "gif_url": "https://exemplo.com/gif.gif"
     }'
```

## Estrutura dos Dados

### Exercício
```json
{
  "id": 1,
  "nome": "Supino Reto",
  "grupo_muscular": "Peito",
  "descricao": "Deite-se no banco e empurre a barra para cima...",
  "equipamento": "Barra e banco",
  "gif_url": "https://exemplo.com/supino.gif"
}
```

### Usuário
```json
{
  "id": 1,
  "username": "admin",
  "email": "admin@trainsmart.com",
  "is_admin": true
}
```

## Como Executar

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Criar Administrador
```bash
python scripts/criar_admin.py
```

### 3. Popular Exercícios (se necessário)
```bash
python scripts/popular_exercicios.py
```

### 4. Iniciar API
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Acessar Documentação
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## Grupos Musculares Disponíveis
- Peito
- Costas  
- Pernas
- Bíceps
- Tríceps
- Ombros
- Abdômen
- Cardio

## Tipos de Equipamento
- Barra e banco
- Peso corporal
- Halteres e banco
- Polia alta
- Barra ou halteres
- Barra olímpica
- Máquina leg press
- Máquina extensora
- Dois bancos
- Halteres
- Nenhum

## Segurança

### ⚠️ Importante para Produção
1. **Alterar SECRET_KEY** em `app/auth.py`
2. **Usar HTTPS** sempre
3. **Configurar CORS** adequadamente
4. **Alterar senha do admin padrão**
5. **Usar variáveis de ambiente** para configurações sensíveis

### Permissões
- **Usuários comuns:** Apenas GET (leitura)
- **Administradores:** CRUD completo (Create, Read, Update, Delete)

## Status Codes
- `200` - Sucesso
- `201` - Criado com sucesso
- `400` - Dados inválidos
- `401` - Não autenticado
- `403` - Sem permissão (não é admin)
- `404` - Recurso não encontrado
- `422` - Erro de validação
