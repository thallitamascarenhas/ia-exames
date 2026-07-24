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
