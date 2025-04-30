from dagster import Definitions

from .environment import dagster_env
from .assets import assets
from .resources import resources
from .jobs import jobs
from .sensors import sensors
from .schedules import schedules


defs = Definitions(
    assets=assets,
    resources=resources(dagster_env),
    jobs=jobs,
    sensors=sensors,
    schedules=schedules,
)
