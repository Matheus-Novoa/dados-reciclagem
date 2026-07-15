with tb_empr_estab as (
	select
		t2.razao_social,
		t1.*,
		t2.desc_porte_empresa
	from {{ref('silver_estabelecimentos')}} as t1
	left join {{ref('silver_empresas')}} as t2
	on t1.cnpj_basico = t2.cnpj_basico
),
tb_nomes_municipios as (
    select
        t1.*,
        t2.descrição as nome_municipio
    from tb_empr_estab as t1
    left join {{ref('silver_municipios')}} as t2
    on t1.codigo_municipio = t2.codigo
    where situacao_cadastral = 2
)
select
	*,
	case
		when uf in ('AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO') then 'NORTE'
        when uf in ('AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE') then 'NORDESTE'
        when uf in ('DF', 'GO', 'MT', 'MS') then 'CENTRO-OESTE'
        when uf in ('ES', 'MG', 'RJ', 'SP') then 'SUDESTE'
        when uf in ('PR', 'RS', 'SC') then 'SUL'
        else 'DESCONHECIDO'
	end as regiao
from tb_nomes_municipios