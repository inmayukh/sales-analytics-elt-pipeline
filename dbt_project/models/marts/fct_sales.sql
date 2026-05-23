{{ config(
    materialized='incremental',
    unique_key='order_id'
) }}

select
    o.order_id,
    o.order_date,

    c.customer_id,
    c.customer_name,
    c.city,

    p.product_id,
    p.product_name,
    p.price,

    o.quantity,

    (o.quantity * p.price) as total_amount

from {{ ref('stg_orders') }} o

join {{ ref('stg_customers') }} c
    on o.customer_id = c.customer_id

join {{ ref('stg_products') }} p
    on o.product_id = p.product_id

{% if is_incremental() %}

where o.order_date >
    (select max(order_date) from {{ this }})

{% endif %}