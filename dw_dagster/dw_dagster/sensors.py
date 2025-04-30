from dagster import(
    asset_sensor, AssetKey, 
    RunRequest, DefaultSensorStatus
)

@asset_sensor(
    asset_key=AssetKey("dwd_customers"), 
    job_name="dws_customers_job", 
    minimum_interval_seconds=5,
    default_status=DefaultSensorStatus.RUNNING,
)
def dwd_customers_sensor():
    return RunRequest()

sensors = [ 
  dwd_customers_sensor,
]