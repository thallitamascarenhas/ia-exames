import streamlit as st
from datetime import date

from database.pacientes import listar_pacientes
from services.exame_service import cadastrar_exame, buscar_exames


st.set_page_config(
    page_title="Novo Exame",
    page_icon="📄"
)


st.title("📄 Novo Exame")


pacientes = listar_pacientes()


if pacientes:

    nomes = [
        paciente["nome"]
        for paciente in pacientes
    ]


    paciente_selecionado = st.selectbox(
        "Selecione o paciente",
        nomes
    )


    paciente = next(
        p for p in pacientes
        if p["nome"] == paciente_selecionado
    )


    data_exame = st.date_input(
        "Data do exame",
        value=date.today()
    )


    laboratorio = st.text_input(
        "Laboratório"
    )


    nome_pdf = st.text_input(
        "Nome do arquivo PDF"
    )


    if st.button("Salvar exame"):

        dados = {

            "paciente_id": paciente["id"],
            "data_exame": data_exame.isoformat(),
            "laboratorio": laboratorio,
            "nome_pdf": nome_pdf

        }


        cadastrar_exame(dados)


        st.success(
            "Exame cadastrado!"
        )


else:

    st.warning(
        "Cadastre um paciente primeiro."
    )



st.divider()

st.subheader("Exames cadastrados")

st.dataframe(
    buscar_exames(),
    use_container_width=True
)
