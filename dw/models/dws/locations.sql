with

locations as (

    select * from {{ ref('dwd_locations') }}

)

select * from locations
