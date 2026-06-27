select * from read_csv(
    '../data/raw/*', -- 👈 Caminho para os seus arquivos ZIP brutos
    header=False,                     -- 👈 Garante que CEP, CNPJ e UF não percam zeros à esquerda
    delim=';',
    auto_detect=False,
    ignore_errors=True,
    null_padding=True,                    -- 👈 Preenche com NULL se faltar alguma coluna no fim da linha
    filename=True,                        -- 👈 Opcional: adiciona uma coluna com o nome do arquivo de origem
    columns={
        'cnpj_basico': 'VARCHAR',
        'cnpj_ordem': 'VARCHAR',
        'cnpj_dv': 'VARCHAR',
        'identificador_matriz_filial': 'VARCHAR',
        'nome_fantasia': 'VARCHAR',
        'situacao_cadastral': 'VARCHAR',
        'data_situacao_cadastral': 'VARCHAR',
        'motivo_situacao_cadastral': 'VARCHAR',
        'nome_cidade_exterior': 'VARCHAR',
        'pais': 'VARCHAR',
        'data_inicio_atividade': 'VARCHAR',
        'cnae_fiscal_principal': 'VARCHAR',
        'cnae_fiscal_secundaria': 'VARCHAR',
        'tipo_logradouro': 'VARCHAR',
        'logradouro': 'VARCHAR',
        'numero': 'VARCHAR',
        'complemento': 'VARCHAR',
        'bairro': 'VARCHAR',
        'cep': 'VARCHAR',
        'uf': 'VARCHAR',
        'municipio': 'VARCHAR',
        'ddd_1': 'VARCHAR',
        'telefone_1': 'VARCHAR',
        'ddd_2': 'VARCHAR',
        'telefone_2': 'VARCHAR',
        'ddd_fax': 'VARCHAR',
        'telefone_fax': 'VARCHAR',
        'correio_eletronico': 'VARCHAR',
        'situacao_especial': 'VARCHAR',
        'data_situacao_especial': 'VARCHAR'
    }
)
where 1=1
and cnae_fiscal_principal='3832700'
or cnae_fiscal_secundaria='3832700'