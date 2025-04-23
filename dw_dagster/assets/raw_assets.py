import os

import pandas as pd
from dagster_duckdb import DuckDBResource
from dagster import AssetExecutionContext, asset
from dw_dagster.project import dw_project


@asset(kinds={"python", "duckdb"})
def raw_customers(context: AssetExecutionContext, duckdb: DuckDBResource) -> None:
    num_rows = raw_jaffle_shop_assets(duckdb, "customers")
    context.add_output_metadata({"num_rows": num_rows})

@asset(kinds={"python", "duckdb"})
def raw_items(context: AssetExecutionContext, duckdb: DuckDBResource) -> None:
    num_rows = raw_jaffle_shop_assets(duckdb, "items")
    context.add_output_metadata({"num_rows": num_rows})

@asset(kinds={"python", "duckdb"})
def raw_orders(context: AssetExecutionContext, duckdb: DuckDBResource) -> None:
    num_rows = raw_jaffle_shop_assets(duckdb, "orders", date_cols=["ordered_at"])
    context.add_output_metadata({"num_rows": num_rows})
    
@asset(kinds={"python", "duckdb"})
def raw_products(context: AssetExecutionContext, duckdb: DuckDBResource) -> None:
    num_rows = raw_jaffle_shop_assets(duckdb, "products")
    context.add_output_metadata({"num_rows": num_rows})

@asset(kinds={"python", "duckdb"})
def raw_stores(context: AssetExecutionContext, duckdb: DuckDBResource) -> None:
    num_rows = raw_jaffle_shop_assets(duckdb, "stores", date_cols=["opened_at"])
    context.add_output_metadata({"num_rows": num_rows})

@asset(kinds={"python", "duckdb"})
def raw_supplies(context: AssetExecutionContext, duckdb: DuckDBResource) -> None:
    num_rows = raw_jaffle_shop_assets(duckdb, "supplies")
    context.add_output_metadata({"num_rows": num_rows})

@asset(kinds={"python", "duckdb"})
def raw_tweets(context: AssetExecutionContext, duckdb: DuckDBResource) -> None:
    num_rows = raw_jaffle_shop_assets(duckdb, "tweets", date_cols=["tweeted_at"])
    context.add_output_metadata({"num_rows": num_rows})


def raw_jaffle_shop_assets(duckdb: DuckDBResource, asset_name, date_cols=[]) -> int:
    assets_csv_file = dw_project.project_dir.joinpath("data", "jaffle-data", f"raw_{asset_name}.csv")
    data = pd.read_csv(os.fspath(assets_csv_file), parse_dates=date_cols)
    
    with duckdb.get_connection() as conn:
      conn.execute("create schema if not exists jaffle_shop")
      conn.execute(
        f"create or replace table jaffle_shop.ods_{asset_name} as select * from data"
      )
    
    return data.shape[0]
