select * from read_csv(
    '../data/raw/F.K03200$Z.D60613.MUNICCSV', -- 👈 Caminho para os seus arquivos ZIP brutos
    header=False,
    delim=';',
    auto_detect=False,
    ignore_errors=True,
    null_padding=True,                    -- 👈 Preenche com NULL se faltar alguma coluna no fim da linha
    filename=True,                        -- 👈 Opcional: adiciona uma coluna com o nome do arquivo de origem
    columns={
        'codigo': 'VARCHAR',
        'descrição': 'VARCHAR'
    }
)