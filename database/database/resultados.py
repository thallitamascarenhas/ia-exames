from database.supabase import supabase


def salvar_resultado(
    exame_id,
    marcador,
    categoria,
    resultado,
    unidade,
    referencia_min,
    referencia_max,
    status
):

    dados = {

        "exame_id": exame_id,
        "marcador": marcador,
        "categoria": categoria,
        "resultado": resultado,
        "unidade": unidade,
        "referencia_min": referencia_min,
        "referencia_max": referencia_max,
        "status": status

    }


    resposta = (
        supabase
        .table("resultados")
        .insert(dados)
        .execute()
    )


    return resposta.data
