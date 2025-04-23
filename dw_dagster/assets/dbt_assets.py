from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from dw_dagster.project import dw_project


@dbt_assets(manifest=dw_project.manifest_path)
def dw_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
