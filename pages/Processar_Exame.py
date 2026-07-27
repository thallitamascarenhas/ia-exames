import streamlit as st

from services.exame_service import buscar_exames, obter_pdf_exame
from services.pdf_service import extrair_texto_pdf


st.title("🔬 Processar exame")


exames = buscar_exames()


if exames:

    opcoes = {
        exame["id"]: exame
        for exame in exames
    }


    exame_id = st.selectbox(
        "Selecione o exame",
        opcoes.keys()
    )


    exame = opcoes[exame_id]


    st.write(
        "Arquivo:",
        exame["nome_pdf"]
    )


    if st.button("Processar"):


        pdf = obter_pdf_exame(
            exame
        )


        texto = extrair_texto_pdf(
            pdf
        )


        st.subheader(
            "Texto extraído"
        )


        st.text(
            texto
        )


else:

    st.warning(
        "Nenhum exame cadastrado."
    )
