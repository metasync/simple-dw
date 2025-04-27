import os
from pathlib import Path


dagster_env = os.getenv("DAGSTER_ENV", "dev")
root_dir = Path(os.getcwd()).resolve()
data_dir = root_dir.joinpath("data").resolve()

environment = {
  "dagster_env": dagster_env,
  "root_dir": root_dir,
  "data_dir": data_dir,
}
