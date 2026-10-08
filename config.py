import pandas as pd

# ============================================================
# ARQUIVO PDF
# ============================================================

PDF_FILENAME = "/home/eliakim/Documents/PR_SL7_414.pdf"


# ============================================================
# PÁGINAS DO PDF
# ============================================================

PAGINAS_DESEJADAS = [6, 7, 8]

# ============================================================
# CONFIGURAÇÕES DO PANDAS
# ============================================================

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', None)


# ============================================================
# COLUNAS NECESSÁRIAS DO PDF
# ============================================================

COLUNAS_DESEJADAS = [
    'ID',
    'From Device',
    'Pin from',
    'To Device',
    'Pin to',
    'Type',
    'Cable_Official_Code',
    'Estimated Length',
    'Modif. Novo'
]