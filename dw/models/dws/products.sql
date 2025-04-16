with

products as (

    select * from {{ ref('dwd_products') }}

)

select * from products
