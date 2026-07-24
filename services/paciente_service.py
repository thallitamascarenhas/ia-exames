from database.pacientes import (
    salvar_paciente,
    listar_pacientes
)


def cadastrar_paciente(dados):

    return salvar_paciente(
        dados["nome"],
        dados["nascimento"],
        dados["sexo"],
        dados["altura"],
        dados["peso"],
        dados["telefone"],
        dados["email"],
        dados["observacoes"]
    )


def buscar_pacientes():

    return listar_pacientes()
