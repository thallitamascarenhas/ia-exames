import streamlit as st
from datetime import date

from database.pacientes import listar_pacientes
from database.storage import upload_pdf
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


    arquivo_pdf = st.file_uploader(
        "Enviar exame PDF",
        type=["pdf"]
    )


    if st.button("Salvar exame"):


        if arquivo_pdf:


            caminho_pdf = upload_pdf(
                arquivo_pdf.getvalue(),
                arquivo_pdf.name
            )


            dados = {

                "paciente_id": paciente["id"],
                "data_exame": data_exame.isoformat(),
                "laboratorio": laboratorio,
                "nome_pdf": caminho_pdf

            }


            exame = cadastrar_exame(
                dados
            )


            st.success(
                "Exame cadastrado com PDF!"
            )


            st.write(
                "ID do exame:",
                exame["id"]
            )


        else:

            st.warning(
                "Selecione um arquivo PDF."
            )


else:

    st.warning(
        "Cadastre um paciente primeiro."
    )



st.divider()


st.subheader(
    "Exames cadastrados"
)


st.dataframe(
    buscar_exames(),
    use_container_width=True
)
