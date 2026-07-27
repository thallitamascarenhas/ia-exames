import re


def extrair_valor_unidade(texto):

    resultados = []


    linhas = [
        linha.strip()
        for linha in texto.split("\n")
        if linha.strip()
    ]


    for i, linha in enumerate(linhas):

        # procura linhas que parecem resultados numéricos
        encontrados = re.search(
            r"([-+]?\d+[,.]?\d*)\s*([a-zA-Zµ/%]+(?:/[a-zA-Z]+)?)?",
            linha
        )


        if encontrados:

            valor = encontrados.group(1)

            unidade = encontrados.group(2)


            valor = valor.replace(",", ".")


            resultados.append(
                {
                    "linha": linha,
                    "valor": float(valor),
                    "unidade": unidade
                }
            )


    return resultados

def extrair_resultado_marcador(texto, nome_marcador):

    linhas = [
        linha.strip()
        for linha in texto.split("\n")
        if linha.strip()
    ]


    for i, linha in enumerate(linhas):

        if linha.lower() == nome_marcador.lower():

            try:

                linha_resultado = linhas[i+1]


                encontrado = re.search(
                    r"([-+]?\d+[,.]?\d*)\s*([a-zA-Zµ/%]+(?:/[a-zA-Z]+)?)?",
                    linha_resultado
                )


                if encontrado:

                    valor = encontrado.group(1)

                    unidade = encontrado.group(2)


                    return {
                        "valor": float(valor.replace(",", ".")),
                        "unidade": unidade
                    }


            except:
                return None


    return None
