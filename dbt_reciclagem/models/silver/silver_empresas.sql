select
    nullif(trim(cnpj_basico), '') as cnpj_basico,
    nullif(upper(trim(razao_social)), '') as razao_social,
    cast(nullif(trim(natureza_juridica), '') as integer) as natureza_juridica,
    cast(nullif(trim(qualificacao_responsavel), '') as integer) as qualificacao_responsavel,
    cast(replace(nullif(trim(capital_social), ''), ',', '.') as decimal(18, 2)) as capital_social,
    cast(nullif(trim(porte_empresa), '') as integer) as porte_empresa,
    nullif(trim(cnpj_basico), '') as cnpj_basico
from {{ ref('bronze_empresas') }}
