import streamlit as st

from services.resultado_service import (
    identificar_marcador,
    buscar_parametro,
    avaliar_resultado
)


st.title("🧪 Teste de interpretação")


valor = st.number_input(
    "Digite o valor",
    value=22
)


if st.button("Avaliar"):

    marcador = identificar_marcador(
        "vitamina d"
    )


    if marcador:

        st.write(
            "Marcador encontrado:"
        )

        st.write(
            marcador
        )


        parametro = buscar_parametro(
            marcador["marcador_id"]
        )


        st.write(
            "Parâmetro:"
        )

        st.write(
            parametro
        )


        resultado = avaliar_resultado(
            valor,
            parametro
        )


        st.success(
            resultado
        )


    else:

        st.error(
            "Marcador não encontrado"
        )
