from pathlib import Path

from dagster_dbt import DbtProject
from .environment import dagster_env

dw_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..", "dw").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
    target=dagster_env,
)
dw_project.prepare_if_dev()
