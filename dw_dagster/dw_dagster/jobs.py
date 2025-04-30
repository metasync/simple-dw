from dagster import define_asset_job, AssetSelection

dws_customers_job = define_asset_job("dws_customers_job", selection="customers")

jobs = [ 
  dws_customers_job,
]