Simple data warehouse

### Setup python project for data warehouse

```
uv init dw
uv add duckdb dbt dbt-duckdb dagster dagster-webserver dagster-duckdb go-task-bin
uv add jafgen --dev
```

To generate 2 years of Jaffle Shop data:
```
jafgen --pre ods 2
```
