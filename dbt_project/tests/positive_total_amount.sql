select *
from {{ ref('fact_orders') }}
where total_amount <= 0