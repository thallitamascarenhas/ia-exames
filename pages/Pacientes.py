import streamlit as st

st.set_page_config(page_title="Pacientes", page_icon="👥")

st.title("👥 Pacientes")

st.write("Cadastro de pacientes")

import streamlit as st

from database.supabase import listar_pacientes

st.title("👥 Pacientes")

dados = listar_pacientes()

st.write(dados)
