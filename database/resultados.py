from database.supabase import supabase


def salvar_resultado(
    exame_id,
    marcador_id,
    categoria,
    resultado,
    valor_numerico,
    unidade,
    referencia_min,
    referencia_max,
    alerta_min,
    alerta_max,
    critico_min,
    critico_max,
    status,
    observacao
):

    dados = {

        "exame_id": exame_id,
        "marcador_id": marcador_id,
        "categoria": categoria,
        "resultado": resultado,
        "valor_numerico": valor_numerico,
        "unidade": unidade,
        "referencia_min": referencia_min,
        "referencia_max": referencia_max,
        "alerta_min": alerta_min,
        "alerta_max": alerta_max,
        "critico_min": critico_min,
        "critico_max": critico_max,
        "status": status,
        "observacao": observacao

    }


    resposta = (
        supabase
        .table("resultados")
        .insert(dados)
        .execute()
    )


    return resposta.data
