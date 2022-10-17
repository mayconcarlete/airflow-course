from airflow import DAG
from datetime import datetime, timedelta

default_args = {
  "owner": "airflow",
  "email_on_failure": False,
  "email_on_retry": False,
  "email": "maycon.carlete@gmail.com",
  "retries": 1,
  "retry_delay": timedelta(minutes=5),
}

with DAG(
  dag_id="forex_data_pipeline",
  start_date=datetime(2021, 1, 1),
  schedule_interval="@daily",
  default_args=default_args,
  catchup=False
) as dag:
  pass