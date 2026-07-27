from services.resultado_service import (
    montar_resultado,
    salvar_resultados,
    buscar_parametro
)

from services.extracao_service import extrair_valor_unidade

import streamlit as st
import pandas as pd

from services.pdf_service import extrair_texto_pdf
from services.resultado_service import encontrar_marcadores


st.title("🔎 Processamento de exame")


arquivo = st.file_uploader(
    "Enviar PDF",
    type=["pdf"]
)


if arquivo:

    texto = extrair_texto_pdf(
        arquivo
    )


    st.subheader("Texto extraído")

    st.text(texto)



    encontrados = encontrar_marcadores(
        texto
    )


    st.subheader("Marcadores encontrados")


    df = pd.DataFrame(encontrados)


    st.dataframe(
        df[
            [
                "nome_padrao",
                "linha",
                "marcador_id"
            ]
        ],
        width="stretch"
    )

    valores = extrair_valor_unidade(texto)


    resultados_salvar = []


    for marcador in encontrados:


        for valor in valores:


            if marcador["linha"] in valor["linha"]:


                parametro = buscar_parametro(
                    marcador["marcador_id"]
                )


                resultado = montar_resultado(

                    exame_id="af05f639-9e72-4df8-a61b-392c8c7df826",

                    marcador_info={
                        "nome_padrao": marcador["nome_padrao"]
                    },

                    valor=valor["valor"],

                    unidade=valor["unidade"],

                    parametro=parametro
                )


                resultados_salvar.append(
                    resultado
                )



    if st.button("Salvar resultados"):


        salvar_resultados(
            resultados_salvar
        )


        st.success(
            "Resultados salvos com sucesso!"
        )


        st.dataframe(
            pd.DataFrame(resultados_salvar)
        )
