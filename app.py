import streamlit as st

from config.settings import *


st.set_page_config(

    page_title=APP_NAME,

    page_icon=PAGE_ICON,

    layout="wide"

)


st.title(PAGE_ICON + " " + APP_NAME)

st.caption(APP_DESCRIPTION)

st.divider()

c1,c2,c3,c4=st.columns(4)

c1.metric("Pacientes","0")

c2.metric("Exames","0")

c3.metric("Resultados","0")

c4.metric("Alertas","0")


st.info(

"Bem-vinda ao Exame Inteligente."

)

from database.supabase import supabase

st.success("Conectado ao Supabase!")
