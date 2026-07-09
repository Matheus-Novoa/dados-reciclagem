select
    cast(nullif(trim(codigo), '') as integer) as codigo,
    nullif(upper(trim(descrição)), '') as descrição,
from {{ ref('bronze_municipios') }}