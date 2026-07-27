import streamlit as st

from services.exame_service import (
    buscar_exames,
    obter_pdf_exame
)

from services.pdf_service import (
    extrair_texto_pdf
)

from services.resultado_service import (
    processar_resultados_exame
)


st.title("🔬 Processar exame")


exames = buscar_exames()


if not exames:

    st.warning(
        "Nenhum exame cadastrado."
    )

else:

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


        resultados = processar_resultados_exame(
            exame["id"],
            texto
        )


        st.subheader(
            "Resultados processados"
        )


        st.dataframe(
            resultados,
            width="stretch"
        )
