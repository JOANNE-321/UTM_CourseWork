import pandas as pd
import psycopg2
from pathlib import Path

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "censo_escolar",
    "user": "censo",
    "password": "123"
}

output_path = Path("data/output")

tables = {
    "dim_year": output_path / "dim_year.csv",
    "dim_school": output_path / "dim_school.csv",
    "dim_location": output_path / "dim_location.csv",
    "dim_education_stage": output_path / "dim_education_stage.csv",
    "fact_school_census": output_path / "fact_school_census.csv"
}

create_table_sql = {
    "dim_year": """
        DROP TABLE IF EXISTS dim_year CASCADE;
        CREATE TABLE dim_year (
            year INTEGER,
            year_id BIGINT PRIMARY KEY
        );
    """,
    "dim_school": """
        DROP TABLE IF EXISTS dim_school CASCADE;
        CREATE TABLE dim_school (
            school_id INTEGER PRIMARY KEY,
            school_name TEXT,
            school_type TEXT
        );
    """,
    "dim_location": """
        DROP TABLE IF EXISTS dim_location CASCADE;
        CREATE TABLE dim_location (
            region TEXT,
            state TEXT,
            city TEXT,
            location_id BIGINT PRIMARY KEY
        );
    """,
    "dim_education_stage": """
        DROP TABLE IF EXISTS dim_education_stage CASCADE;
        CREATE TABLE dim_education_stage (
            education_stage TEXT,
            education_stage_id BIGINT PRIMARY KEY
        );
    """,
    "fact_school_census": """
        DROP TABLE IF EXISTS fact_school_census CASCADE;
        CREATE TABLE fact_school_census (
            year_id BIGINT,
            school_id INTEGER,
            location_id BIGINT,
            education_stage_id BIGINT,
            student_count INTEGER,
            teacher_count INTEGER
        );
    """
}

def load_csv_to_table(cursor, table_name, csv_file):
    df = pd.read_csv(csv_file)

    columns = list(df.columns)
    placeholders = ", ".join(["%s"] * len(columns))
    column_names = ", ".join(columns)

    insert_sql = f"""
        INSERT INTO {table_name} ({column_names})
        VALUES ({placeholders})
    """

    for _, row in df.iterrows():
        cursor.execute(insert_sql, tuple(row))

    print(f"Loaded {len(df)} rows into {table_name}")

def main():
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    for table_name, sql in create_table_sql.items():
        cursor.execute(sql)
        print(f"Created table: {table_name}")

    for table_name, csv_file in tables.items():
        load_csv_to_table(cursor, table_name, csv_file)

    conn.commit()
    cursor.close()
    conn.close()

    print("All CSV files loaded into PostgreSQL successfully.")

if __name__ == "__main__":
    main()