from database.exames import (
    salvar_exame,
    listar_exames,
    buscar_exame_por_id
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
def obter_exame(exame_id):

    return buscar_exame_por_id(
        exame_id
    )
