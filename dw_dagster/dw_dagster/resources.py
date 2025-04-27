from dagster_dbt import DbtCliResource

from .project import dw_project

dbt_resource = DbtCliResource(project_dir=dw_project)

resources_by_env = {
  "dev": {
    "dbt": dbt_resource,
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

