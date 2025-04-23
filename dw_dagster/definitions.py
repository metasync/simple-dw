import os
from dagster_duckdb import DuckDBResource

from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets.dbt_assets import dw_dbt_assets
from .assets.raw_assets import (
    raw_customers, raw_items, raw_orders, raw_products, 
    raw_stores, raw_supplies, raw_tweets
)
from .project import dw_project
from .schedules import schedules

defs = Definitions(
    assets=[
        raw_customers, 
        raw_items,
        raw_orders,
        raw_products,
        raw_stores,
        raw_supplies,
        raw_tweets,
        dw_dbt_assets
    ],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=dw_project),
        "duckdb": DuckDBResource(
            database=os.fspath(dw_project.project_dir.joinpath("data", "dev.duckdb")),
        )
    },
)
