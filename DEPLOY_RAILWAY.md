# TrainSmart API - Deploy para Railway

## 🚀 Deploy Automático

### 1. Preparação
```bash
# 1. Criar conta no Railway (https://railway.app)
# 2. Conectar repositório GitHub
# 3. Criar novo projeto
```

### 2. Configurar Variáveis de Ambiente no Railway

No painel do Railway, vá em `Variables` e adicione:

```bash
# OBRIGATÓRIO - Gere uma chave segura
SECRET_KEY=sua_chave_super_segura_aqui_32_caracteres_minimo

# Configuração do Admin
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@seudominio.com
ADMIN_PASSWORD=sua_senha_super_segura

# Ambiente
ENVIRONMENT=production

# CORS - Especifique seus domínios
ALLOWED_ORIGINS=https://seuapp.vercel.app,https://seudominio.com

# Database (Railway providencia automaticamente)
# DATABASE_URL será criada automaticamente pelo Railway PostgreSQL
```

### 3. Deploy

O Railway detectará automaticamente o `Dockerfile` e fará deploy automaticamente.

## 🔒 Checklist de Segurança

### ✅ Antes do Deploy
- [ ] SECRET_KEY única e segura (32+ caracteres)
- [ ] ADMIN_PASSWORD forte
- [ ] ALLOWED_ORIGINS específicos (não usar *)
- [ ] ENVIRONMENT=production
- [ ] Docs desabilitadas em produção
- [ ] Database em produção (PostgreSQL)

### ✅ Após Deploy
- [ ] Health check funcionando: `https://seuapp.railway.app/health`
- [ ] Criar admin: `https://seuapp.railway.app/auth/token`
- [ ] Testar endpoints públicos
- [ ] Verificar logs
- [ ] Configurar monitoramento

## 🌐 URLs de Produção

```
API Base: https://seuapp.railway.app
Health: https://seuapp.railway.app/health
Exercícios: https://seuapp.railway.app/exercicios
Login: https://seuapp.railway.app/auth/token
```

## 📊 Monitoramento

### Logs
```bash
# No painel Railway, acessar "Deployments" > "View Logs"
```

### Métricas Importantes
- Response time < 200ms
- CPU usage < 80%
- Memory usage < 80%
- Error rate < 1%

### Alertas
Configure alertas para:
- Falhas de deploy
- Alto uso de recursos
- Erros 5xx
- Downtime
