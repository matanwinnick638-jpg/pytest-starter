import re

def extract_table_names_fallback(sql_text):
    # Common SQL keywords that are followed by table names
    patterns = [
        r"FROM\s+\[?([\w\.]+)\]?",
        r"JOIN\s+\[?([\w\.]+)\]?",
        r"INTO\s+\[?([\w\.]+)\]?",
        r"UPDATE\s+\[?([\w\.]+)\]?",
        r"INSERT\s+INTO\s+\[?([\w\.]+)\]?",
        r"DELETE\s+FROM\s+\[?([\w\.]+)\]?",
        r"MERGE\s+INTO\s+\[?([\w\.]+)\]?",
        r"EXEC\s+\[?([\w\.]+)\]?",
    ]

    tables = set()
    for pattern in patterns:
        matches = re.findall(pattern, sql_text, flags=re.IGNORECASE)
        tables.update(matches)

    return sorted(tables)

if __name__ == "__main__":
    path = "4.08.00.02_MERGED_202507251624224016.sql"
    with open(path, encoding="utf-8") as f:
        sql_text = f.read()

    tables = extract_table_names_fallback(sql_text)

    print("✅ Tables found:")
    for t in tables:
        print(" -", t)
