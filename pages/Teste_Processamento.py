import streamlit as st
import pandas as pd

from services.pdf_service import extrair_texto_pdf
from services.resultado_service import encontrar_marcadores


st.title("🔎 Processamento de exame")


arquivo = st.file_uploader(
    "Enviar PDF",
    type=["pdf"]
)


if arquivo:

    texto = extrair_texto_pdf(
        arquivo
    )


    st.subheader("Texto extraído")

    st.text(texto)



    encontrados = encontrar_marcadores(
        texto
    )


    st.subheader("Marcadores encontrados")


    df = pd.DataFrame(encontrados)


    st.dataframe(
        df[
            [
                "nome_padrao",
                "linha",
                "marcador_id"
            ]
        ],
        width="stretch"
    )
