CSS_STYLES = """
<style>
.stApp {
    background-color: #F2F4F8;
    color: #0F172A;
    font-family: Inter, system-ui, sans-serif;
}

[data-testid="stWidgetLabel"] {
    color: #0F172A !important;
    font-weight: 600;
}

.dashboard-header {
    background: linear-gradient(135deg, #111827 0%, #1F2937 100%);
    color: #ffffff;
    padding: 24px 28px;
    font-size: 26px;
    font-weight: 700;
    border-radius: 18px;
    margin-bottom: 24px;
    box-shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
}

.metrics-row {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 18px;
    margin-bottom: 24px;
}

.metric-card {
    background-color: #ffffff;
    border-radius: 18px;
    padding: 22px;
    box-shadow: 0 14px 32px rgba(15, 23, 42, 0.08);
    border: 1px solid rgba(148, 163, 184, 0.16);
}

.metric-label {
    color: #475569;
    font-size: 0.9rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.metric-value {
    font-size: 2.25rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 10px;
}

.metric-note {
    color: #64748b;
    font-size: 0.95rem;
}

.section-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: #0f172a;
    margin-top: 28px;
    margin-bottom: 14px;
}

.stDataFrameContainer {
    background: transparent;
}

[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
    border: 1px solid rgba(148, 163, 184, 0.16);
    background-color: #ffffff;
}

.dashboard-table-container [data-testid="stDataFrame"] {
    width: 100%;
    background-color: #ffffff;
}

.dashboard-table-container [data-testid="stDataFrame"] table {
    border-collapse: collapse;
    width: 100%;
}

.dashboard-table-container [data-testid="stDataFrame"] th {
    background-color: #FBBF24 !important;
    color: #0F172A !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    padding: 16px 18px !important;
}

.dashboard-table-container [data-testid="stDataFrame"] td {
    color: #334155 !important;
    padding: 14px 18px !important;
    border-bottom: 1px solid rgba(148, 163, 184, 0.12) !important;
}

.dashboard-table-container [data-testid="stDataFrame"] tr:nth-child(even) {
    background-color: #F8FAFC !important;
}

.dashboard-table-container [data-testid="stDataFrame"] tr:hover {
    background-color: rgba(251, 191, 36, 0.14) !important;
}

.st-bg {
    background-color: transparent;
}

.dashboard-table-container {
    width: 100%;
    max-width: 100%;
    overflow-x: auto;
    border-radius: 18px;
    box-shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
    background-color: #ffffff;
    border: 1px solid rgba(148, 163, 184, 0.16);
    margin-top: 0.5rem;
    padding: 4px;
    box-sizing: border-box;
}

.dashboard-table {
    width: 100%;
    max-width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
}

.dashboard-table th,
.dashboard-table td {
    padding: 10px 12px;
    white-space: normal;
    word-break: break-word;
    overflow-wrap: anywhere;
    vertical-align: top;
    font-size: 0.92rem;
}

.dashboard-table th {
    font-size: 0.8rem;
}

.dashboard-table th:first-child {
    width: 28%;
}

.dashboard-table th:nth-child(2) {
    width: 24%;
}

.dashboard-table th:nth-child(3),
.dashboard-table th:nth-child(4),
.dashboard-table th:nth-child(5) {
    width: 16%;
}

.dashboard-table td:first-child {
    width: 28%;
}

.dashboard-table td:nth-child(2) {
    width: 24%;
}

.dashboard-table td:nth-child(3),
.dashboard-table td:nth-child(4),
.dashboard-table td:nth-child(5) {
    width: 16%;
}


.dashboard-table thead th {
    background-color: #FBBF24;
    color: #0F172A;
    font-weight: 700;
    font-size: 0.95rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    border-bottom: none;
    text-align: center;
}

.dashboard-table tbody tr:nth-child(odd) {
    background-color: #ffffff;
}

.dashboard-table tbody tr:nth-child(even) {
    background-color: #F8FAFC;
}

.dashboard-table tbody tr:hover {
    background-color: rgba(251, 191, 36, 0.14);
}

.dashboard-table td {
    color: #334155;
    border-bottom: 1px solid rgba(148, 163, 184, 0.12);
}

.dashboard-table td:first-child {
    text-align: left;
    font-weight: 600;
}

.dashboard-table td:not(:first-child) {
    text-align: center;
}
</style>
"""


import pandas as pd
import streamlit as st


def render_dashboard_header(title: str) -> None:
    st.markdown(
        f'<div class="dashboard-header">{title}</div>',
        unsafe_allow_html=True,
    )


# def render_metrics_section(cards: list[tuple[str, int, str]]) -> None:
#     cols = st.columns(len(cards), gap="large")

#     for col, (label, value, note) in zip(cols, cards):
#         with col:
#             st.markdown(
#                 f"""
#                 <div class="metric-card">
#                     <div class="metric-label">{label}</div>
#                     <div class="metric-value">{value}</div>
#                     <div class="metric-note">{note}</div>
#                 </div>
#                 """,
#                 unsafe_allow_html=True,
#             )


def render_section_title(title: str) -> None:
    st.markdown(
        f'<div class="section-title">{title}</div>',
        unsafe_allow_html=True,
    )


def render_data_table(
    df: pd.DataFrame,
    columns: list[str] | None = None,
    column_labels: dict[str, str] | None = None,
) -> None:
    if columns is not None:
        df = df.loc[:, columns]

    if column_labels is None:
        column_labels = {}

    display_df = df.copy()
    if column_labels:
        display_df = display_df.rename(columns=column_labels)

    header_cells = "".join(
        f'<th>{column_labels.get(col, col.title().replace("_", " "))}</th>'
        for col in display_df.columns
    )

    body_rows = []
    for _, row in display_df.iterrows():
        row_cells = "".join(
            f'<td>{row[col] if pd.notna(row[col]) else ""}</td>'
            for col in display_df.columns
        )
        body_rows.append(f"<tr>{row_cells}</tr>")

    table_html = f"""
    <div class="dashboard-table-container">
        <table class="dashboard-table">
            <thead>
                <tr>{header_cells}</tr>
            </thead>
            <tbody>
                {''.join(body_rows)}
            </tbody>
        </table>
    </div>
    """

    st.markdown(table_html, unsafe_allow_html=True)
