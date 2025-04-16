with

supplies as (

    select * from {{ ref('dwd_supplies') }}

)

select * from supplies
