# 🚀 TrainSmart API - GUIA COMPLETO DE DEPLOY PARA PRODUÇÃO

## ✅ **IMPLEMENTAÇÕES DE SEGURANÇA CONCLUÍDAS**

### 🔐 **Segurança Implementada**
- ✅ **Variáveis de ambiente** para dados sensíveis
- ✅ **Configurações dinâmicas** baseadas no ambiente
- ✅ **Headers de segurança** (XSS, CSRF, etc.)
- ✅ **CORS restritivo** para produção
- ✅ **Documentação desabilitada** em produção
- ✅ **Usuário não-root** no Docker
- ✅ **Health checks** implementados
- ✅ **Logging estruturado**
- ✅ **Registro de admin protegido** em produção

## 🌐 **OPÇÕES DE DEPLOY**

### **1. 🚂 Railway (RECOMENDADO - Mais Fácil)**

#### Preparação:
```bash
# 1. Criar conta: https://railway.app
# 2. Conectar GitHub
# 3. Criar novo projeto
# 4. Deploy automático do Dockerfile
```

#### Variáveis no Railway:
```bash
SECRET_KEY=sua_chave_super_segura_32_caracteres_minimo
ENVIRONMENT=production
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@seudominio.com
ADMIN_PASSWORD=sua_senha_super_segura_123
ALLOWED_ORIGINS=https://seuapp.vercel.app,https://seudominio.com
LOG_LEVEL=INFO
```

### **2. 🐳 Docker Local/VPS**

```bash
# Clone o repositório
git clone seu-repo
cd trainsmart_api

# Copie e configure variáveis
cp .env.example .env.production
# Edite .env.production com valores de produção

# Deploy
chmod +x deploy.sh
./deploy.sh
```

### **3. ☁️ Heroku**

```bash
# Instalar Heroku CLI
# Login: heroku login

# Criar app
heroku create trainsmart-api

# Configurar variáveis
heroku config:set SECRET_KEY=sua_chave_super_segura
heroku config:set ENVIRONMENT=production
heroku config:set ADMIN_PASSWORD=senha_segura

# Deploy
git push heroku main
```

### **4. 🌊 DigitalOcean App Platform**

```yaml
# app.yaml
name: trainsmart-api
services:
- name: api
  source_dir: /
  github:
    repo: seu-usuario/trainsmart-api
    branch: main
  run_command: uvicorn app.main:app --host 0.0.0.0 --port 8080
  environment_slug: python
  instance_count: 1
  instance_size_slug: basic-xxs
  envs:
  - key: SECRET_KEY
    value: sua_chave_super_segura
  - key: ENVIRONMENT
    value: production
  - key: ADMIN_PASSWORD
    value: senha_segura
```

## 🔒 **CHECKLIST DE SEGURANÇA OBRIGATÓRIO**

### **⚠️ ANTES DO DEPLOY**
- [ ] **SECRET_KEY** única gerada (32+ caracteres)
- [ ] **ADMIN_PASSWORD** forte (12+ caracteres, números, símbolos)
- [ ] **ALLOWED_ORIGINS** específicos (nunca usar "*")
- [ ] **ENVIRONMENT=production**
- [ ] **Banco PostgreSQL** configurado (se aplicável)
- [ ] **SSL/HTTPS** configurado
- [ ] **.env** no .gitignore

### **⚠️ APÓS DEPLOY**
- [ ] Health check funcionando: `/health`
- [ ] Login admin funcionando: `/auth/token`
- [ ] Endpoints públicos funcionando
- [ ] Documentação desabilitada (404 em `/docs`)
- [ ] Headers de segurança presentes
- [ ] Logs funcionando
- [ ] Backup configurado

## 🧪 **TESTES PÓS-DEPLOY**

```bash
# Health Check
curl https://sua-api.railway.app/health

# Login Admin
curl -X POST "https://sua-api.railway.app/auth/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=admin&password=sua_senha"

# Teste público
curl "https://sua-api.railway.app/exercicios/"

# Verificar docs desabilitadas (deve retornar 404)
curl https://sua-api.railway.app/docs
```

## 📊 **MONITORAMENTO**

### **Métricas Importantes**
- **Response Time:** < 200ms
- **CPU Usage:** < 80%
- **Memory Usage:** < 512MB
- **Error Rate:** < 1%
- **Uptime:** > 99.9%

### **Logs para Monitorar**
```bash
# Erros críticos
ERROR:
CRITICAL:

# Tentativas de login
POST /auth/token

# Operações de admin
POST /exercicios/
PUT /exercicios/
DELETE /exercicios/
```

### **Alertas Configurar**
- Falhas de deploy
- Alto uso de recursos
- Erros 5xx
- Tentativas de acesso não autorizado

## 🔄 **MANUTENÇÃO**

### **Backup Semanal**
```bash
# Backup do banco (se SQLite)
cp exercicios.db backup_$(date +%Y%m%d).db

# Backup via API (recomendado)
curl "https://sua-api.railway.app/exercicios/" > backup_exercicios.json
```

### **Updates Regulares**
```bash
# Atualizar dependências
pip install --upgrade -r requirements.txt

# Rebuild e redeploy
# (automaticamente no Railway via Git push)
```

### **Rotação de Senhas**
- **Mensal:** Admin password
- **Trimestral:** SECRET_KEY
- **Anual:** Certificados SSL

## 🚨 **RECUPERAÇÃO DE DESASTRES**

### **Se API ficar fora do ar:**
1. Verificar logs da plataforma
2. Verificar health check
3. Verificar variáveis de ambiente
4. Rollback para versão anterior
5. Restaurar backup se necessário

### **Se banco corromper:**
1. Parar aplicação
2. Restaurar backup mais recente
3. Executar script popular_exercicios.py
4. Recriar admin
5. Reiniciar aplicação

## 📞 **SUPORTE**

### **Recursos de Debug**
- Logs da aplicação
- Health check endpoint
- Métricas da plataforma
- Error tracking (Sentry recomendado)

---

## 🎯 **DEPLOY RECOMENDADO: RAILWAY**

**Mais simples e eficiente para sua API:**

1. **Criar conta:** https://railway.app
2. **Conectar GitHub**
3. **Configurar variáveis** (lista acima)
4. **Deploy automático!**

**Sua API estará online em minutos com:**
- ✅ HTTPS automático
- ✅ Health checks
- ✅ Logs centralizados  
- ✅ Auto-scaling
- ✅ Backup automático
- ✅ Zero-downtime deploys

**Pronto para receber milhares de requisições! 🚀**
