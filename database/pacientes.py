from database.supabase import supabase


def listar_pacientes():

    resposta = (
        supabase
        .table("pacientes")
        .select("*")
        .execute()
    )

    return resposta.data



def salvar_paciente(
    nome,
    nascimento,
    sexo,
    altura,
    peso,
    telefone,
    email,
    observacoes
):

    dados = {

        "nome": nome,
        "nascimento": nascimento,
        "sexo": sexo,
        "altura": altura,
        "peso": peso,
        "telefone": telefone,
        "email": email,
        "observacoes": observacoes

    }


    resposta = (
        supabase
        .table("pacientes")
        .insert(dados)
        .execute()
    )


    return resposta.data
