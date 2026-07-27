import streamlit as st

from services.pdf_service import extrair_texto_pdf
from services.processamento_service import processar_exame


st.title("🧠 Processamento completo do exame")


arquivo = st.file_uploader(
    "Enviar PDF",
    type=["pdf"]
)


if arquivo:


    texto = extrair_texto_pdf(
        arquivo
    )


    resultados = processar_exame(
        texto
    )


    st.subheader("Resultados encontrados")


    st.dataframe(
        resultados,
        width="stretch"
    )
