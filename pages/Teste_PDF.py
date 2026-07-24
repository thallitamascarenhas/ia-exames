import streamlit as st

from services.pdf_service import extrair_texto_pdf


st.title("🧪 Teste leitura PDF")


arquivo = st.file_uploader(
    "Enviar PDF",
    type=["pdf"]
)


if arquivo:

    texto = extrair_texto_pdf(
        arquivo
    )

    st.text_area(
        "Texto extraído",
        texto,
        height=400
    )
