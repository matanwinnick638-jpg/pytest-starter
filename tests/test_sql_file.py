from src.sql_utils import load_sql_file

def test_sql_file_matches_reference():
    test_sql = load_sql_file("path/to/4.08.00.02_MERGED_202507251624224016.sql")
    reference_sql = load_sql_file("path/to/reference_script.sql")

    assert test_sql == reference_sql
