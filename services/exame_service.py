from database.exames import (
    salvar_exame,
    listar_exames
)


def cadastrar_exame(dados):

    return salvar_exame(
        dados["paciente_id"],
        dados["data_exame"],
        dados["laboratorio"],
        dados["nome_pdf"]
    )



def buscar_exames():

    return listar_exames()
