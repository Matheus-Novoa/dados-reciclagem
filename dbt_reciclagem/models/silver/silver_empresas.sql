with tb_int as (
    select
        nullif(trim(cnpj_basico), '') as cnpj_basico,
        nullif(upper(trim(razao_social)), '') as razao_social,
        cast(nullif(trim(natureza_juridica), '') as integer) as natureza_juridica,
        cast(nullif(trim(qualificacao_responsavel), '') as integer) as qualificacao_responsavel,
        cast(replace(nullif(trim(capital_social), ''), ',', '.') as decimal(18, 2)) as capital_social,
        cast(nullif(trim(porte_empresa), '') as integer) as cod_porte_empresa,
        -- case
        --     when cast(nullif(trim(porte_empresa), '') as integer) = 0 then 'NÃO INFORMADO'
        --     when cast(nullif(trim(porte_empresa), '') as integer) = 1 then 'MICRO EMPRESA'
        --     when cast(nullif(trim(porte_empresa), '') as integer) = 3 then 'EMPRESA DE PEQUENO PORTE'
        --     when cast(nullif(trim(porte_empresa), '') as integer) = 5 then 'DEMAIS'
        -- end as desc_porte_empresa,
        nullif(trim(ente_federativo), '') as ente_federativo
    from {{ ref('bronze_empresas') }}
)

select
    *,
    case
        when cod_porte_empresa = 0 then 'NÃO INFORMADO'
        when cod_porte_empresa = 1 then 'MICRO EMPRESA'
        when cod_porte_empresa = 3 then 'EMPRESA DE PEQUENO PORTE'
        when cod_porte_empresa = 5 then 'DEMAIS'
    end as desc_porte_empresa
from tb_int