import re

from database.supabase import supabase
from database.resultados import salvar_resultado

def converter_numero(texto):

    texto = texto.strip()

    # Ex.: 8.450
    if "." in texto and "," not in texto:

        partes = texto.split(".")

        if len(partes[-1]) == 3:

            texto = texto.replace(".", "")

    # Ex.: 11,1
    texto = texto.replace(",", ".")

    return float(texto)

def buscar_parametro(marcador_id):

    resposta = (
        supabase
        .table("parametros_referencia")
        .select("*")
        .eq(
            "marcador_id",
            marcador_id
        )
        .execute()
    )

    if resposta.data:
        return resposta.data[0]

    return None



def interpretar(valor, parametro):

    if valor <= parametro["critico_min"]:
        return "Crítico baixo"

    if valor < parametro["valor_min"]:
        return "Abaixo do recomendado"

    if valor <= parametro["valor_max"]:
        return "Normal"

    if valor <= parametro["critico_max"]:
        return "Acima do recomendado"

    return "Crítico alto"



def listar_sinonimos():

    resposta = (
        supabase
        .table("sinonimos_marcadores")
        .select(
            """
            sinonimo,
            marcador_id,
            marcadores(
                nome_padrao
            )
            """
        )
        .execute()
    )

    return resposta.data



def encontrar_marcadores(texto):

    encontrados = []

    sinonimos = listar_sinonimos()


    linhas = [
        linha.strip()
        for linha in texto.split("\n")
        if linha.strip()
    ]


    for linha in linhas:

        for item in sinonimos:

            sinonimo = item["sinonimo"].lower().strip()


            if linha.lower().strip() == sinonimo:


                existe = any(
                    x["marcador_id"] == item["marcador_id"]
                    for x in encontrados
                )


                if not existe:

                    encontrados.append(
                        {
                            "linha": linha,
                            "marcador_id": item["marcador_id"],
                            "nome_padrao": item["marcadores"]["nome_padrao"]
                        }
                    )


    return encontrados



def processar_resultados_exame(
    exame_id,
    texto
):


    resultados_salvos = []


    linhas = [
        linha.strip()
        for linha in texto.split("\n")
        if linha.strip()
    ]


    marcadores = encontrar_marcadores(
        texto
    )



    for marcador in marcadores:


        valor_encontrado = None


        for i, linha in enumerate(linhas):


            if linha == marcador["nome_padrao"]:


                if i + 1 < len(linhas):

                    valor_linha = linhas[i+1]


                    resultado = re.search(
                        r"([-+]?\d+[,.]?\d*)\s*([a-zA-Zµ/%]+)?",
                        valor_linha
                    )


                    if resultado:


                        "valor": converter_numero(
    resultado.group(1)
),

                            "unidade": resultado.group(2)

                        }


                break



        if not valor_encontrado:

            continue



        parametro = buscar_parametro(
            marcador["marcador_id"]
        )



        if parametro:


            status = interpretar(
                valor_encontrado["valor"],
                parametro
            )


            categoria = status


        else:

            status = "Sem parâmetro"

            categoria = "Não avaliado"



        dados = {


            "exame_id": exame_id,

            "marcador_id": marcador["marcador_id"],

            "categoria": categoria,

            "resultado": str(
                valor_encontrado["valor"]
            ),

            "valor_numerico": valor_encontrado["valor"],

            "unidade": valor_encontrado["unidade"],


            "referencia_min": parametro["valor_min"]
            if parametro else None,


            "referencia_max": parametro["valor_max"]
            if parametro else None,


            "alerta_min": parametro["alerta_min"]
            if parametro else None,


            "alerta_max": parametro["alerta_max"]
            if parametro else None,


            "critico_min": parametro["critico_min"]
            if parametro else None,


            "critico_max": parametro["critico_max"]
            if parametro else None,


            "status": status,


            "observacao": parametro["observacao"]
            if parametro else None

        }



        salvar_resultado(

            dados["exame_id"],

            dados["marcador_id"],

            dados["categoria"],

            dados["resultado"],

            dados["valor_numerico"],

            dados["unidade"],

            dados["referencia_min"],

            dados["referencia_max"],

            dados["alerta_min"],

            dados["alerta_max"],

            dados["critico_min"],

            dados["critico_max"],

            dados["status"],

            dados["observacao"]

        )


        resultados_salvos.append(
            dados
        )


    return resultados_salvos
