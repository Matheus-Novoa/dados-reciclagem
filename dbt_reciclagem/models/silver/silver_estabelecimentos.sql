select
    nullif(trim(cnpj_basico), '') as cnpj_basico,
    nullif(trim(cnpj_ordem), '') as cnpj_ordem,
    nullif(trim(cnpj_dv), '') as cnpj_dv,
    cast(identificador_matriz_filial as integer) as identificador_matriz_filial,
    nullif(upper(trim(nome_fantasia)), '') as nome_fantasia,
    cast(nullif(trim(situacao_cadastral), '') as integer) as situacao_cadastral,
    nullif(upper(trim(nome_cidade_exterior)), '') as nome_cidade_exterior,
    cast(nullif(trim(pais), '') as integer) as codigo_pais,
    case
        when nullif(trim(data_inicio_atividade), '') in ('00000000', '') then null
        else strptime(data_inicio_atividade, '%Y%m%d')::date
    end as data_inicio_atividade,
    lpad(trim(cnae_fiscal_principal), 7, '0') as cnae_fiscal_principal,
    nullif(trim(cnae_fiscal_secundaria), '') as cnae_fiscal_secundaria,
    nullif(upper(trim(tipo_logradouro)), '') as tipo_logradouro,
    nullif(upper(trim(logradouro)), '') as logradouro,
    nullif(trim(numero), '') as numero,
    nullif(upper(trim(complemento)), '') as complemento,
    nullif(upper(trim(bairro)), '') as bairro,
    lpad(regexp_replace(trim(cep), '[^0-9]', '', 'g'), 8, '0') as cep,
    cast(nullif(trim(municipio), '') as integer) as codigo_municipio,
    nullif(lower(trim(correio_eletronico)), '') as correio_eletronico,
    nullif(upper(trim(uf)), '') as uf
from {{ ref('bronze_estabelecimentos') }}
