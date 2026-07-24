import streamlit as st
from datetime import date

from services.paciente_service import (
    cadastrar_paciente,
    buscar_pacientes
)


st.set_page_config(
    page_title="Pacientes",
    page_icon="👥"
)


st.title("👥 Cadastro de Pacientes")


with st.form("form_paciente"):

    nome = st.text_input(
        "Nome completo"
    )

    nascimento = st.date_input(
        "Data de nascimento",
        min_value=date(1900, 1, 1),
        max_value=date.today()
    )

    sexo = st.selectbox(
        "Sexo",
        [
            "Feminino",
            "Masculino",
            "Outro"
        ]
    )

    altura = st.number_input(
        "Altura (cm)",
        min_value=0
    )

    peso = st.number_input(
        "Peso (kg)",
        min_value=0.0
    )

    telefone = st.text_input(
        "Telefone"
    )

    email = st.text_input(
        "Email"
    )

    observacoes = st.text_area(
        "Observações"
    )


    salvar = st.form_submit_button(
        "💾 Salvar paciente"
    )


    if salvar:

        dados = {

    "nome": nome,
    "nascimento": nascimento.isoformat(),
    "sexo": sexo,
    "altura": altura,
    "peso": peso,
    "telefone": telefone,
    "email": email,
    "observacoes": observacoes

}


cadastrar_paciente(dados)

        st.success(
            "Paciente cadastrado com sucesso!"
        )


st.divider()


st.subheader(
    "Pacientes cadastrados"
)


dados = buscar_pacientes()


st.dataframe(
    dados,
    use_container_width=True
)
