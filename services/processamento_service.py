from services.resultado_service import (
    encontrar_marcadores,
    buscar_parametro,
    interpretar
)

from services.extracao_service import (
    extrair_resultado_marcador
)



def processar_exame(texto):

    resultados = []


    marcadores = encontrar_marcadores(texto)


    for marcador in marcadores:


        nome = marcador["nome_padrao"]

        marcador_id = marcador["marcador_id"]


        valor_unidade = extrair_resultado_marcador(
            texto,
            nome
        )


        if valor_unidade is None:
            continue


        valor = valor_unidade["valor"]

        unidade = valor_unidade["unidade"]


        parametro = buscar_parametro(
            marcador_id
        )


        if parametro:

            status = interpretar(
                valor,
                parametro
            )

        else:

            status = "Sem parâmetro"



        resultados.append(
            {
                "marcador_id": marcador_id,
                "marcador": nome,
                "valor": valor,
                "unidade": unidade,
                "status": status
            }
        )


    return resultados
