import fitz


def extrair_texto_pdf(arquivo_pdf):

    if hasattr(arquivo_pdf, "read"):

        arquivo = arquivo_pdf.read()

    else:

        arquivo = arquivo_pdf


    documento = fitz.open(
        stream=arquivo,
        filetype="pdf"
    )


    texto = ""


    for pagina in documento:

        texto += pagina.get_text()


    return texto
