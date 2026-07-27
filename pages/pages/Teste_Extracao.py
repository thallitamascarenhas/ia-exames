import streamlit as st

from services.pdf_service import extrair_texto_pdf
from services.extracao_service import extrair_valor_unidade


st.title("🧪 Teste extração de valores")


arquivo = st.file_uploader(
    "Enviar PDF",
    type=["pdf"]
)


if arquivo:

    texto = extrair_texto_pdf(
        arquivo
    )


    resultados = extrair_valor_unidade(
        texto
    )


    st.subheader("Valores encontrados")


    st.dataframe(
        resultados,
        width="stretch"
    )
