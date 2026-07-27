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
