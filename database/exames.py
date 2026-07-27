from database.supabase import supabase


def listar_exames():

    resposta = (
        supabase
        .table("exames")
        .select("*")
        .execute()
    )

    return resposta.data



def salvar_exame(
    paciente_id,
    data_exame,
    laboratorio,
    nome_pdf
):

    dados = {

        "paciente_id": paciente_id,
        "data_exame": data_exame,
        "laboratorio": laboratorio,
        "nome_pdf": nome_pdf

    }


    resposta = (
        supabase
        .table("exames")
        .insert(dados)
        .execute()
    )

    return resposta.data[0]

def buscar_exame_por_id(exame_id):

    resposta = (
        supabase
        .table("exames")
        .select("*")
        .eq(
            "id",
            exame_id
        )
        .execute()
    )


    if resposta.data:

        return resposta.data[0]


    return None
