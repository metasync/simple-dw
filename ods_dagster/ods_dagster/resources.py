import os

from dagster_duckdb import DuckDBResource

from .environment import data_dir

resources_by_env = {
  "dev": {
    "duckdb": 
      DuckDBResource(
        database=os.fspath(data_dir.joinpath("dev.duckdb"))
      ),
  },
  "snd": {},
  "prod": {}
}

def resources(dagster_env: str):
  return resources_by_env[dagster_env]
