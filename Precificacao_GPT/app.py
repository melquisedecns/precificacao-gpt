
import streamlit as st
from etapa1 import etapa1_premissas
from etapa2 import etapa2_custos
from etapa3 import etapa3_dados_base
from etapa4 import etapa4_func
from etapa5 import etapa5_valores

st.set_page_config(page_title="Sistema de Precificação", layout="wide")

# Logo e título
st.image("Logo Mplan Soluções.png", width=250)
st.title("📊 Sistema de Precificação de Serviços")

# Inicialização de variáveis
dados_script = {}
dados_etapa2 = {}
dados_equipes = []
dados_frota = []
dados_miscelaneas = []
dados_etapa4 = {}
dados_etapa5 = {}

# Menu lateral
etapa = st.sidebar.radio("Etapas", ["Etapa 1", "Etapa 2", "Etapa 3", "Etapa 4", "Etapa 5"])

if etapa == "Etapa 1":
    dados_script = etapa1_premissas()

elif etapa == "Etapa 2":
    if dados_script:
        dados_etapa2 = etapa2_custos(dados_script)
    else:
        st.warning("⚠️ Por favor, preencha primeiro a Etapa 1.")

elif etapa == "Etapa 3":
    dados_equipes, dados_frota, dados_miscelaneas = etapa3_dados_base()

elif etapa == "Etapa 4":
    if dados_script and dados_equipes and dados_frota:
        etapa4_func()
    else:
        st.warning("⚠️ Complete as etapas anteriores.")

elif etapa == "Etapa 5":
    if dados_etapa2:
        etapa5_valores(dados_etapa2)
    else:
        st.warning("⚠️ Preencha os custos na Etapa 2 antes de continuar.")
