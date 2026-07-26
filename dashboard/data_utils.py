from pathlib import Path

import duckdb
import pandas as pd
import streamlit as st


@st.cache_data
def carregar_dados(parquet_path: str | None = None) -> pd.DataFrame:
    """Carrega os dados do parquet para o dashboard."""
    if parquet_path is None:
        parquet_path = Path(__file__).resolve().parents[1] / "data" / "gold" / "dim_estabelecimentos.parquet"
    else:
        parquet_path = Path(parquet_path)

    df = duckdb.query(f"SELECT * FROM '{parquet_path}'").df()
    return df
