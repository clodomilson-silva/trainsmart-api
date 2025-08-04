import requests
import json

# Configuração da API
BASE_URL = "http://localhost:8000"

def test_public_endpoints():
    """Testa endpoints públicos (sem autenticação)"""
    print("🔍 Testando endpoints públicos...")
    
    # Listar todos os exercícios
    response = requests.get(f"{BASE_URL}/exercicios/")
    print(f"GET /exercicios/ - Status: {response.status_code}")
    if response.status_code == 200:
        exercicios = response.json()
        print(f"📋 Total de exercícios: {len(exercicios)}")
    
    # Testar filtros
    response = requests.get(f"{BASE_URL}/exercicios/?grupo_muscular=Peito")
    print(f"GET /exercicios/?grupo_muscular=Peito - Status: {response.status_code}")
    if response.status_code == 200:
        exercicios = response.json()
        print(f"💪 Exercícios de peito: {len(exercicios)}")
    
    # Listar grupos musculares
    response = requests.get(f"{BASE_URL}/exercicios/grupos-musculares")
    print(f"GET /exercicios/grupos-musculares - Status: {response.status_code}")
    if response.status_code == 200:
        grupos = response.json()
        print(f"🎯 Grupos musculares: {grupos}")
    
    # Listar equipamentos
    response = requests.get(f"{BASE_URL}/exercicios/equipamentos")
    print(f"GET /exercicios/equipamentos - Status: {response.status_code}")
    if response.status_code == 200:
        equipamentos = response.json()
        print(f"🏋️ Equipamentos: {equipamentos}")

def test_admin_login():
    """Testa login de administrador"""
    print("\n🔐 Testando login de administrador...")
    
    login_data = {
        "username": "admin",
        "password": "admin123"
    }
    
    response = requests.post(
        f"{BASE_URL}/auth/token",
        data=login_data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    
    print(f"POST /auth/token - Status: {response.status_code}")
    
    if response.status_code == 200:
        token_data = response.json()
        token = token_data["access_token"]
        print("✅ Login bem-sucedido!")
        return token
    else:
        print("❌ Falha no login")
        print(response.text)
        return None

def test_admin_operations(token):
    """Testa operações de administrador"""
    if not token:
        print("❌ Token não disponível para testar operações de admin")
        return
    
    print("\n🛠️ Testando operações de administrador...")
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # Criar novo exercício
    novo_exercicio = {
        "nome": "Teste API",
        "grupo_muscular": "Teste",
        "descricao": "Exercício criado via API para teste",
        "equipamento": "Nenhum",
        "gif_url": "https://exemplo.com/teste.gif"
    }
    
    response = requests.post(
        f"{BASE_URL}/exercicios/",
        json=novo_exercicio,
        headers=headers
    )
    
    print(f"POST /exercicios/ - Status: {response.status_code}")
    
    if response.status_code == 200:
        exercicio_criado = response.json()
        exercicio_id = exercicio_criado["id"]
        print(f"✅ Exercício criado com ID: {exercicio_id}")
        
        # Atualizar exercício
        exercicio_atualizado = novo_exercicio.copy()
        exercicio_atualizado["nome"] = "Teste API Atualizado"
        
        response = requests.put(
            f"{BASE_URL}/exercicios/{exercicio_id}",
            json=exercicio_atualizado,
            headers=headers
        )
        
        print(f"PUT /exercicios/{exercicio_id} - Status: {response.status_code}")
        
        # Deletar exercício
        response = requests.delete(
            f"{BASE_URL}/exercicios/{exercicio_id}",
            headers=headers
        )
        
        print(f"DELETE /exercicios/{exercicio_id} - Status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Exercício deletado com sucesso!")
    else:
        print("❌ Falha ao criar exercício")
        print(response.text)

def test_unauthorized_access():
    """Testa acesso não autorizado"""
    print("\n🚫 Testando acesso não autorizado...")
    
    # Tentar criar exercício sem token
    novo_exercicio = {
        "nome": "Teste Não Autorizado",
        "grupo_muscular": "Teste",
        "descricao": "Não deveria funcionar",
        "equipamento": "Nenhum",
        "gif_url": "https://exemplo.com/teste.gif"
    }
    
    response = requests.post(
        f"{BASE_URL}/exercicios/",
        json=novo_exercicio,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"POST /exercicios/ (sem token) - Status: {response.status_code}")
    
    if response.status_code == 401:
        print("✅ Acesso negado corretamente!")
    else:
        print("❌ Falha na segurança - acesso deveria ser negado")

if __name__ == "__main__":
    print("🚀 Iniciando testes da TrainSmart API...\n")
    
    # Testa endpoints públicos
    test_public_endpoints()
    
    # Testa login de admin
    token = test_admin_login()
    
    # Testa operações de admin
    test_admin_operations(token)
    
    # Testa acesso não autorizado
    test_unauthorized_access()
    
    print("\n✅ Testes concluídos!")
