from pathlib import Path

from dagster_dbt import DbtProject

dw_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "dw").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "simple-dw").resolve(),
)
dw_project.prepare_if_dev()
