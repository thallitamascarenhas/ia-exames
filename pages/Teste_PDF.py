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

    st.subheader("Texto extraído")

    st.text_area(
        "",
        texto,
        height=400
    )
