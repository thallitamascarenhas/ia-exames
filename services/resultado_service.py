import re


def extrair_resultados(texto):

    linhas = [
        linha.strip()
        for linha in texto.split("\n")
        if linha.strip()
    ]

    resultados = []


    for i, linha in enumerate(linhas):

        if linha in [
            "Glicose",
            "Hemoglobina",
            "Hematócrito",
            "Leucócitos",
            "Neutrófilos",
            "Linfócitos",
            "Plaquetas",
            "Ferritina",
            "Ferro sérico",
            "Vitamina B12",
            "Vitamina D",
            "TSH",
            "T4 Livre",
            "Creatinina",
            "Ureia",
            "AST (TGO)",
            "ALT (TGP)",
            "Colesterol Total",
            "HDL",
            "LDL",
            "Triglicerídeos",
            "PCR"
        ]:

            marcador = linha

            resultado = linhas[i+1]

            referencia = linhas[i+2]

            status = linhas[i+3]


            resultados.append(
                {
                    "marcador": marcador,
                    "resultado": resultado,
                    "referencia": referencia,
                    "status": status
                }
            )


    return resultados

from database.supabase import supabase


def identificar_marcador(nome):
    
    nome = nome.lower().strip()


    resposta = (
        supabase
        .table("sinonimos_marcadores")
        .select(
            """
            marcador_id,
            marcadores(
                nome_padrao
            )
            """
        )
        .ilike(
            "sinonimo",
            nome
        )
        .execute()
    )


    if resposta.data:

        return resposta.data[0]


    return None

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


def avaliar_resultado(valor, parametro):

    if valor < parametro["critico_max"]:
        return "Crítico baixo"


    if valor < parametro["valor_min"]:
        return "Alerta baixo"


    if valor <= parametro["valor_max"]:
        return "Normal"


    if valor <= parametro["alerta_max"]:
        return "Alerta alto"


    return "Crítico alto"

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
from database.supabase import supabase


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

        linha_normalizada = linha.lower()


        for item in sinonimos:

            sinonimo = item["sinonimo"].lower().strip()


            if linha_normalizada == sinonimo:


                ja_existe = any(
                    encontrado["marcador_id"] == item["marcador_id"]
                    for encontrado in encontrados
                )


                if not ja_existe:

                    encontrados.append(
                        {
                            "linha": linha,
                            "marcador_id": item["marcador_id"],
                            "nome_padrao": item["marcadores"]["nome_padrao"]
                        }
                    )


    return encontrados

def salvar_resultado(resultado):

    resposta = (
        supabase
        .table("resultados")
        .insert(resultado)
        .execute()
    )

    return resposta.data
def montar_resultado(
    exame_id,
    marcador_info,
    valor,
    unidade,
    parametro
):

    status = "Sem parâmetro"


    if parametro:

        status = interpretar(
            valor,
            parametro
        )


    resultado = {

        "exame_id": exame_id,

        "marcador": marcador_info["nome_padrao"],

        "categoria": "Laboratorial",

        "resultado": str(valor),

        "unidade": unidade,

        "referencia_min": (
            parametro["valor_min"]
            if parametro
            else None
        ),

        "referencia_max": (
            parametro["valor_max"]
            if parametro
            else None
        ),

        "status": status
    }


    return resultado

def salvar_resultados(lista_resultados):

    resposta = (
        supabase
        .table("resultados")
        .insert(lista_resultados)
        .execute()
    )

    return resposta.data

