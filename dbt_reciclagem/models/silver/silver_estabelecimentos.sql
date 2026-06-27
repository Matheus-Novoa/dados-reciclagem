select
    cnpj_basico,
    cnpj_ordem,
    cnpj_dv,
    identificador_matriz_filial,
    nome_fantasia,
    situacao_cadastral,
    nome_cidade_exterior,
    pais,
    data_inicio_atividade,
    cnae_fiscal_principal,
    cnae_fiscal_secundaria,
    tipo_logradouro,
    logradouro,
    numero,
    complemento,
    bairro,
    cep,
    uf,
    municipio,
    correio_eletronico
from {{ source('bronze_receita', 'bronze_estabelecimentos') }}
--from read_parquet('../data/bronze/bronze_estabelecimentos.parquet')
