from database.supabase import supabase


def upload_pdf(arquivo, nome_arquivo):

    caminho = f"exames/{nome_arquivo}"


    resposta = (
        supabase
        .storage
        .from_("exames")
        .upload(
            caminho,
            arquivo
        )
    )


    return caminho
