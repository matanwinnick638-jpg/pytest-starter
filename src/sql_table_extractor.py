import sqlglot
from sqlglot.errors import ParseError

def extract_table_names(sql_text):
    table_names = set()

    try:
        statements = sqlglot.parse(sql_text)
    except ParseError as e:
        print("Parsing error:", e)
        return set()

    for stmt in statements:
        for table in stmt.find_all(sqlglot.exp.Table):
            table_names.add(table.sql())

    return sorted(table_names)
