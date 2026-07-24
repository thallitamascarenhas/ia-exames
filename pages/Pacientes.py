import streamlit as st

from database.pacientes import (
    salvar_paciente,
    listar_pacientes
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
        "Data de nascimento"
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

        salvar_paciente(
            nome,
            nascimento.isoformat(),
            sexo,
            altura,
            peso,
            telefone,
            email,
            observacoes
        )


        st.success(
            "Paciente cadastrado com sucesso!"
        )



st.divider()


st.subheader(
    "Pacientes cadastrados"
)


dados = listar_pacientes()


st.dataframe(
    dados,
    use_container_width=True
)
