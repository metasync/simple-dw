import os

from dagster_dbt import DbtCliResource
# from dagster_duckdb import DuckDBResource

from .environment import data_dir
from .project import dw_project

dbt_resource = DbtCliResource(project_dir=dw_project)

resources_by_env = {
  "dev": {
    "dbt": dbt_resource,
    # "duckdb": DuckDBResource(database=os.fspath(data_dir.joinpath("dev.duckdb")))
  },
  "snd": {
    "dbt": dbt_resource,
  },
  "prod": {
    "dbt": dbt_resource,
  }
}

def resources(dagster_env: str):
  return resources_by_env[dagster_env]

