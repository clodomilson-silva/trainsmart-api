import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import SessionLocal
from app.models import Exercicio
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

exercicios = [
    # Peito
    {
        "nome": "Supino Reto",
        "grupo_muscular": "Peito",
        "descricao": "Deite-se no banco e empurre a barra para cima, depois desça controladamente até o peito.",
        "equipamento": "Barra e banco",
        "gif_url": "https://www.mundoboaforma.com.br/wp-content/uploads/2020/12/supino-reto.gif"
    },
    {
        "nome": "Flexão de Braço",
        "grupo_muscular": "Peito",
        "descricao": "Corpo reto, desça até o peito quase tocar o chão e empurre de volta.",
        "equipamento": "Peso corporal",
        "gif_url": "https://www.mundoboaforma.com.br/wp-content/uploads/2021/03/flexao-de-bracos-com-apoio-do-antebraco-no-chao.gif"
    },
    {
        "nome": "Crucifixo com Halteres",
        "grupo_muscular": "Peito",
        "descricao": "Abra os braços com halteres e traga-os de volta acima do peito.",
        "equipamento": "Halteres e banco",
        "gif_url": "https://www.hipertrofia.org/blog/wp-content/uploads/2023/09/dumbbell-fly.gif"
    },

    # Costas
    {
        "nome": "Puxada na Frente",
        "grupo_muscular": "Costas",
        "descricao": "Puxe a barra da polia até a parte superior do peito.",
        "equipamento": "Polia alta",
        "gif_url": "https://i.pinimg.com/originals/7e/d3/fd/7ed3fd50a771c125a2fe8adcf3b7eae4.gif"
    },
    {
        "nome": "Remada Curvada",
        "grupo_muscular": "Costas",
        "descricao": "Incline o tronco e puxe a barra ou halteres até o abdômen.",
        "equipamento": "Barra ou halteres",
        "gif_url": "https://www.mundoboaforma.com.br/wp-content/uploads/2020/12/costas-remada-curvada-.gif"
    },
    {
        "nome": "Levantamento Terra",
        "grupo_muscular": "Costas",
        "descricao": "Levante a barra do chão mantendo a coluna neutra e suba em pé.",
        "equipamento": "Barra olímpica",
        "gif_url": "https://www.hipertrofia.org/blog/wp-content/uploads/2017/11/barbell-deadlift.gif"
    },

    # Pernas
    {
        "nome": "Agachamento Livre",
        "grupo_muscular": "Pernas",
        "descricao": "Agache mantendo o tronco reto e desça até formar 90° com os joelhos.",
        "equipamento": "Barra ou halteres",
        "gif_url": "https://www.mundoboaforma.com.br/wp-content/uploads/2020/11/agachamento-livre-1.gif"
    },
    {
        "nome": "Leg Press",
        "grupo_muscular": "Pernas",
        "descricao": "Empurre a plataforma com os pés até estender as pernas.",
        "equipamento": "Máquina leg press",
        "gif_url": "https://media.tenor.com/e0qeS17dv7QAAAAM/legpress45-leg-press.gif"
    },
    {
        "nome": "Cadeira Extensora",
        "grupo_muscular": "Pernas",
        "descricao": "Estenda as pernas usando o quadríceps.",
        "equipamento": "Máquina extensora",
        "gif_url": "https://media.tenor.com/fNeMiJuGmEcAAAAM/cadeira-extensora-extensora.gif"
    },
    {
        "nome": "Afundo",
        "grupo_muscular": "Pernas",
        "descricao": "Dê um passo à frente e agache mantendo o tronco reto.",
        "equipamento": "Halteres ou peso corporal",
        "gif_url": "https://www.mundoboaforma.com.br/wp-content/uploads/2021/04/pernas-afundo-tradicional-sem-pesos-1.gif"
    },

    # Bíceps
    {
        "nome": "Rosca Direta",
        "grupo_muscular": "Bíceps",
        "descricao": "Flexione os cotovelos levantando a barra até o nível do peito.",
        "equipamento": "Barra",
        "gif_url": "https://www.mundoboaforma.com.br/wp-content/uploads/2022/09/rosca-biceps-direta-com-barra-e-pegada-fechada-mulher.gif"
    },
    {
        "nome": "Rosca Martelo",
        "grupo_muscular": "Bíceps",
        "descricao": "Flexione os cotovelos com halteres em posição neutra.",
        "equipamento": "Halteres",
        "gif_url": "https://www.hipertrofia.org/blog/wp-content/uploads/2023/04/dumbbell-hammer-curl-v-2.gif"
    },

    # Tríceps
    {
        "nome": "Tríceps Corda",
        "grupo_muscular": "Tríceps",
        "descricao": "Empurre a corda da polia para baixo separando as mãos no final.",
        "equipamento": "Polia baixa com corda",
        "gif_url": "https://www.mundoboaforma.com.br/wp-content/uploads/2021/07/triceps-puxada-no-pulley-com-corda.gif"
    },
    {
        "nome": "Mergulho entre bancos",
        "grupo_muscular": "Tríceps",
        "descricao": "Apoie as mãos atrás do corpo e desça o tronco flexionando os cotovelos.",
        "equipamento": "Dois bancos",
        "gif_url": "https://www.mundoboaforma.com.br/wp-content/uploads/2021/04/triceps-no-banco.gif"
    },

    # Ombros
    {
        "nome": "Elevação Lateral",
        "grupo_muscular": "Ombros",
        "descricao": "Eleve os braços lateralmente até a altura dos ombros.",
        "equipamento": "Halteres",
        "gif_url": "https://media.tenor.com/cy46UbnfUrkAAAAM/eleva%C3%A7%C3%A3o-lateral-hateres.gif"
    },
    {
        "nome": "Desenvolvimento com Halteres",
        "grupo_muscular": "Ombros",
        "descricao": "Empurre os halteres acima da cabeça mantendo controle.",
        "equipamento": "Halteres",
        "gif_url": "https://www.treinoemalta.com.br/wp-content/uploads/2023/07/Desenvolvimento-com-Halteres-H.gif"
    },

    # Abdômen
    {
        "nome": "Prancha Isométrica",
        "grupo_muscular": "Abdômen",
        "descricao": "Fique apoiado nos cotovelos e pontas dos pés mantendo o corpo reto.",
        "equipamento": "Peso corporal",
        "gif_url": "https://newlabsvita.com.br/wp-content/uploads/2017/08/Prancha-Treinamento-Funcional.jpg"
    },
    {
        "nome": "Abdominal Supra",
        "grupo_muscular": "Abdômen",
        "descricao": "Flexione o tronco em direção aos joelhos deitado no chão.",
        "equipamento": "Peso corporal ou anilha",
        "gif_url": "https://www.mundoboaforma.com.br/wp-content/uploads/2023/02/47271301-abdominal-supra.gif"
    },

    # Cardio
    {
        "nome": "Corrida Estacionária",
        "grupo_muscular": "Cardio",
        "descricao": "Simule corrida sem sair do lugar, levantando bem os joelhos.",
        "equipamento": "Nenhum",
        "gif_url": "https://www.mundoboaforma.com.br/wp-content/uploads/2023/11/31991301-corrida-estacionaria-360.gif"
    },
    {
        "nome": "Polichinelo",
        "grupo_muscular": "Cardio",
        "descricao": "Abra e feche as pernas enquanto bate as mãos acima da cabeça.",
        "equipamento": "Peso corporal",
        "gif_url": "https://www.mundoboaforma.com.br/wp-content/uploads/2021/04/polichinelos.gif"
    }
]

db = SessionLocal()

try:
    # Verificar se já existem exercícios
    total_existentes = db.query(Exercicio).count()
    print(f"📊 Exercícios existentes no banco: {total_existentes}")
    
    novos_exercicios = 0
    for ex in exercicios:
        existe = db.query(Exercicio).filter(Exercicio.nome == ex["nome"]).first()
        if not existe:
            novo = Exercicio(**ex)
            db.add(novo)
            novos_exercicios += 1
            print(f"➕ Adicionado: {ex['nome']}")
    
    db.commit()
    
    total_final = db.query(Exercicio).count()
    print(f"✅ População concluída!")
    print(f"📈 Novos exercícios adicionados: {novos_exercicios}")
    print(f"📊 Total de exercícios no banco: {total_final}")
    
except Exception as e:
    print(f"❌ Erro ao popular exercícios: {e}")
    db.rollback()
finally:
    db.close()
