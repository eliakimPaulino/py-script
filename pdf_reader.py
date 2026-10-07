import pdfplumber
import pandas as pd

from circuit import Circuito
import config


def encontrar_cabecalho(tabela):
    """
    Procura a linha que contém a coluna ID.
    Retorna o índice da linha do cabeçalho.
    """

    for i, row in enumerate(tabela):

        valores = [
            str(cell).strip()
            for cell in row
            if cell is not None
        ]

        if 'ID' in valores:
            return i

    return None


def preparar_dataframe(tabela, linha_cabecalho):
    """
    Transforma a tabela extraída pelo pdfplumber
    em um DataFrame organizado.
    """

    df = pd.DataFrame(tabela)

    # Define o cabeçalho
    df.columns = [
        str(col).strip().replace('\n', ' ')
        if col is not None else ''
        for col in df.iloc[linha_cabecalho]
    ]
    
    df.columns = [
        col.replace('Cable_ Official_Code', 'Cable_Official_Code')
        for col in df.columns
    ]

    # Remove tudo que vem antes do cabeçalho
    df = df[
        linha_cabecalho + 1:
    ].reset_index(drop=True)

    return df

def converter_comprimento(valor):
    """
    Converte o comprimento vindo do PDF
    para float.
    """

    if valor is None:
        return 0.0

    valor = str(valor).strip()

    if not valor:
        return 0.0

    valor = valor.replace(',', '.')

    return float(valor)


def criar_circuito(row):

    id_val = str(row['ID']).strip()

    origem = (
        f"{row['From Device']}/"
        f"{row['Pin from']}"
    )

    destino = (
        f"{row['To Device']}/"
        f"{row['Pin to']}"
    )

    cable_dtr = str(
        row['Cable_Official_Code']
    ).strip()

    diameter = str(
        row['Type']
    ).strip()
    
    modification = str(
            row['Modif. Novo']
        ).strip()

    length = converter_comprimento(row['Estimated Length'])

    return Circuito(
        id=id_val,
        origem=origem,
        destino=destino,
        cable_dtr=cable_dtr,
        diameter=diameter,
        length=length,
        modification=modification
    )


def ler_pagina(pdf, numero_pagina):

    indice_pagina = numero_pagina - 1

    total_paginas = len(pdf.pages)

    if not (0 <= indice_pagina < total_paginas):

        print(
            f"Aviso: Página {numero_pagina} é inválida. "
            f"O PDF possui {total_paginas} páginas."
        )

        return []

    pagina = pdf.pages[indice_pagina]

    tabela = pagina.extract_table()

    if not tabela:

        print(
            f"Nenhuma tabela encontrada "
            f"na página {numero_pagina}."
        )

        return []

    linha_cabecalho = encontrar_cabecalho(tabela)

    if linha_cabecalho is None:

        print(
            f"Não foi possível encontrar o cabeçalho "
            f"na página {numero_pagina}."
        )

        return []

    df = preparar_dataframe(
        tabela,
        linha_cabecalho
    )

    # Verifica se todas as colunas necessárias existem
    colunas_existentes = [
        coluna
        for coluna in config.COLUNAS_DESEJADAS
        if coluna in df.columns
    ]

    if len(colunas_existentes) != len(
        config.COLUNAS_DESEJADAS
    ):

        print(
            f"Algumas colunas não foram encontradas "
            f"na página {numero_pagina}."
        )

        print(
            f"Colunas disponíveis: {list(df.columns)}"
        )

        return []

    # Seleciona apenas as colunas necessárias
    df = df[
        config.COLUNAS_DESEJADAS
    ]

    # Remove linhas com ID "+"
    df = df[
        df['ID']
        .fillna('')
        .astype(str)
        .str.strip() != '+'
    ].reset_index(drop=True)

    circuitos = []

    for _, row in df.iterrows():

        id_val = str(row['ID']).strip()

        # Ignora linhas vazias
        if not id_val or id_val == 'nan':
            continue

        circuito = criar_circuito(row)

        circuitos.append(circuito)

    return circuitos


def ler_pdf():

    lista_circuitos = []

    try:

        with pdfplumber.open(
            config.PDF_FILENAME
        ) as pdf:

            for numero_pagina in config.PAGINAS_DESEJADAS:

                circuitos = ler_pagina(
                    pdf,
                    numero_pagina
                )

                lista_circuitos.extend(
                    circuitos
                )

    except FileNotFoundError:

        print(
            f"O arquivo {config.PDF_FILENAME} "
            f"não foi encontrado."
        )

    return lista_circuitos