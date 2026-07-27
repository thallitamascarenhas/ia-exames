import streamlit as st

from services.resultado_service import (
    identificar_marcador,
    buscar_parametro,
    interpretar
)


st.title("🧪 Processar exame")


valor = st.number_input(
    "Valor vitamina D",
    value=22
)


if st.button("Processar"):


    marcador = identificar_marcador(
        "vitamina d"
    )


    parametro = buscar_parametro(
        marcador["marcador_id"]
    )


    status = interpretar(
        valor,
        parametro
    )


    st.write(
        "Marcador:",
        marcador
    )

    st.write(
        "Parâmetro:",
        parametro
    )

    st.success(status)
