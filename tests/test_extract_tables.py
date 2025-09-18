from src.sql_table_extractor import extract_table_names

def test_list_tables_in_sql():
    with open("path/to/4.08.00.02_MERGED_202507251624224016.sql", encoding="utf-8") as f:
        sql_text = f.read()

    tables = extract_table_names(sql_text)

    print("Tables found:", tables)

    assert "your_expected_table" in tables  # replace with known table
