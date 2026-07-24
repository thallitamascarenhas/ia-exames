import streamlit as st

st.set_page_config(
    page_title="Exame Inteligente",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Exame Inteligente")

st.subheader("Sua plataforma inteligente para análise de exames laboratoriais")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👥 Pacientes", "0")

with col2:
    st.metric("📄 Exames", "0")

with col3:
    st.metric("📈 Tendências", "0")

st.markdown("---")

st.info(
    "Bem-vinda! Este sistema armazenará o histórico dos pacientes, analisará exames laboratoriais e identificará tendências utilizando inteligência artificial."
)
