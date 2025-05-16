import os
from dotenv import load_dotenv

load_dotenv()

def collect_names(sheet):
    column_name = os.getenv("COLUNA_NOME")
    column_type = os.getenv("COLNA_VALOR")
    minimun_value = int(os.getenv("VALOR_MINIMO", 0))

    data = sheet.get_all_values()
    header = data[0]

    col_index_value = ord(column_type.upper()) - ord("A")
    col_index_name = header.index(column_name)

    names = []
    for row in data[1:]:
        try:
            value = int(row[col_index_value])
            if value > minimun_value:
                names.append(row[col_index_name])
        except (ValueError, IndexError):
            continue
    return names