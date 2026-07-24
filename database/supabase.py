from supabase import create_client
import streamlit as st

@st.cache_resource
def conectar():

    url = st.secrets["SUPABASE_URL"]

    key = st.secrets["SUPABASE_KEY"]

    return create_client(url, key)
    
def listar_pacientes():

    supabase = conectar()

    resposta = supabase.table("pacientes").select("*").execute()

    return resposta.data
