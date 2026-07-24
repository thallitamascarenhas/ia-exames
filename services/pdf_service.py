import fitz


def extrair_texto_pdf(caminho_pdf):

    documento = fitz.open(caminho_pdf)

    texto = ""

    for pagina in documento:
        texto += pagina.get_text()

    documento.close()

    return texto
