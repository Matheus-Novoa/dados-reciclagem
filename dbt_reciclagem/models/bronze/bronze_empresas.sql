select * from read_csv(
    '../data/raw/*.EMPRECSV', -- 👈 Caminho para os seus arquivos ZIP brutos
    header=False,
    delim=';',
    auto_detect=False,
    ignore_errors=True,
    null_padding=True,                    -- 👈 Preenche com NULL se faltar alguma coluna no fim da linha
    filename=True,                        -- 👈 Opcional: adiciona uma coluna com o nome do arquivo de origem
    columns={
        'cnpj_basico': 'VARCHAR',
        'razao_social': 'VARCHAR',
        'natureza_juridica': 'VARCHAR',
        'qualificacao_responsavel': 'VARCHAR',
        'capital_social': 'VARCHAR',
        'porte_empresa': 'VARCHAR',
        'ente_federativo': 'VARCHAR'
    }
)