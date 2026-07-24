import streamlit as st

from services.resultado_service import (
    identificar_marcador,
    buscar_parametro,
    avaliar_resultado
)


st.title("🧪 Teste de Interpretação")


valor = st.number_input(
    "Valor do exame",
    value=22.0
)


if st.button("Avaliar"):

    marcador = identificar_marcador(
        "vitamina d"
    )


    if marcador:

        nome = marcador["marcadores"]["nome_padrao"]


        parametro = buscar_parametro(
            marcador["marcador_id"]
        )


        resultado = avaliar_resultado(
            valor,
            parametro
        )


        st.subheader(nome)


        col1, col2 = st.columns(2)


        col1.metric(
            "Resultado",
            f"{valor} {parametro['unidade']}"
        )


        col2.metric(
            "Classificação",
            resultado
        )


        st.info(
            parametro["observacao"]
        )


    else:

        st.error(
            "Marcador não encontrado"
        )
