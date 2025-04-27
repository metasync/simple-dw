from dagster import Definitions

from .environment import dagster_env
from .assets import dw_dbt_assets
from .schedules import schedules
from .resources import resources

defs = Definitions(
    assets=[dw_dbt_assets],
    schedules=schedules,
    resources=resources(dagster_env),
)
