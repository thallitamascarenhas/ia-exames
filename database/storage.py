import uuid

from database.supabase import supabase


def upload_pdf(arquivo, nome):

    nome_unico = f"{uuid.uuid4()}_{nome}"

    caminho = f"exames/{nome_unico}"


    supabase.storage.from_("exames").upload(
        caminho,
        arquivo
    )


    return caminho
