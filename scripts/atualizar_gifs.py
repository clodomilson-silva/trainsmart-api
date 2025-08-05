import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import SessionLocal
from app.models import Exercicio

# URLs corrigidas dos exercícios
exercicios_atualizados = {
    "Crucifixo com Halteres": "https://www.mundoboaforma.com.br/wp-content/uploads/2019/11/03081301-crucifixo-com-halteres.gif",
    "Puxada na Frente": "https://www.mundoboaforma.com.br/wp-content/uploads/2020/12/costas-puxada-aberta-com-barra-no-pulley.gif",
    "Levantamento Terra": "https://www.mundoboaforma.com.br/wp-content/uploads/2020/12/pernas-e-costas-levantamento-terra-deadlift.gif",
    "Rosca Martelo": "https://www.mundoboaforma.com.br/wp-content/uploads/2020/12/rosca-biceps-martelo-com-halteres.gif",
    "Desenvolvimento com Halteres": "https://www.mundoboaforma.com.br/wp-content/uploads/2020/12/desenvolvimento-para-ombros-com-halteres.gif",
    "Prancha Isométrica": "https://www.mundoboaforma.com.br/wp-content/uploads/2020/11/01431301-Bridge-straight-arm_Waist_360_logo.gif"
}

db = SessionLocal()

try:
    print("🔄 Atualizando URLs dos GIFs dos exercícios...")
    
    exercicios_atualizados_count = 0
    
    for nome_exercicio, nova_url in exercicios_atualizados.items():
        exercicio = db.query(Exercicio).filter(Exercicio.nome == nome_exercicio).first()
        
        if exercicio:
            exercicio.gif_url = nova_url
            exercicios_atualizados_count += 1
            print(f"✅ Atualizado: {nome_exercicio}")
        else:
            print(f"⚠️  Exercício não encontrado: {nome_exercicio}")
    
    db.commit()
    print(f"\n🎉 Atualização concluída!")
    print(f"📊 Total de exercícios atualizados: {exercicios_atualizados_count}")
    
except Exception as e:
    print(f"❌ Erro ao atualizar exercícios: {e}")
    db.rollback()
finally:
    db.close()
