import duckdb
from pathlib import Path
from tqdm import tqdm


TEMPLATE_QUERY = 'gen-parquet-bronze.sql'

zip_files = list(Path('data/raw').glob('*.zip'))

for zip_file in tqdm(zip_files):

    with open(TEMPLATE_QUERY, encoding='utf-8') as f:
        query = f.read().format(estab_zip=zip_file.name)

    with duckdb.connect() as con:
        con.execute("INSTALL zipfs FROM community;")
        con.execute("LOAD zipfs;")

        con.execute(F"""
            COPY (
                {query}
            ) TO 'data/bronze/{zip_file.stem}.parquet'
            (FORMAT PARQUET, COMPRESSION 'zstd')
        """)
