import fitz


def extrair_texto_pdf(arquivo_pdf):

    documento = fitz.open(
        stream=arquivo_pdf.read(),
        filetype="pdf"
    )

    texto = ""

    for pagina in documento:
        texto += pagina.get_text()

    documento.close()

    return texto
