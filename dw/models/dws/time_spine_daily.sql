{{
    config(
        materialized = 'table'
    )
}}

with

base_dates as (
    {{
        dbt_utils.date_spine(
            datepart = "day",
            start_date = ("cast('" ~ var("min_time_spine_date") ~ "' as date)"),
            end_date =  ("cast('" ~ var("max_time_spine_date") ~ "' as date)"),
        )
    }}
),

final as (
    select
        cast(date_day as date) as date_day
    from base_dates
)

select * from final
