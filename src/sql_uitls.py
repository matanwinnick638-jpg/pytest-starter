import sqlparse

def load_and_normalize_sql(path):
    with open(path, 'r', encoding='utf-8') as f:
        raw_sql = f.read()
    return sqlparse.format(raw_sql, keyword_case='lower', strip_comments=True).strip()
