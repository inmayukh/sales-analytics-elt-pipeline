{{ config(
    materialized='incremental',
    unique_key='order_id'
) }}

select
    o.order_id,
    o.customer_id,
    c.customer_name,
    c.city,
    o.product_id,
    p.product_name,
    p.price,
    o.quantity,
    (p.price * o.quantity) as total_amount,
    case
    when quantity >= 2 then 'bulk'
    else 'single'
end as order_type,
    o.order_date
from {{ ref('stg_orders') }} o
left join {{ ref('stg_customers') }} c
    on o.customer_id = c.customer_id
left join {{ ref('stg_products') }} p
    on o.product_id = p.product_id

{% if is_incremental() %}

where o.order_date >
    (select max(order_date) from {{ this }})

{% endif %}