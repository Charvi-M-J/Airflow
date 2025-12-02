from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import pandas as pd
import json

def extract_data(**context):
    data = {"id": [1, 2], "price": [100, 200]}
    df = pd.DataFrame(data)
    context["ti"].xcom_push(key="raw_data", value=df.to_json())

def transform_data(**context):
    raw_json = context["ti"].xcom_pull(key="raw_data")
    df = pd.DataFrame(json.loads(raw_json))
    df["price_with_tax"] = df["price"] * 1.18
    context["ti"].xcom_push(key="transformed_data", value=df.to_json())

def load_data(**context):
    final_json = context["ti"].xcom_pull(key="transformed_data")
    df = pd.DataFrame(json.loads(final_json))
    print("Loaded Data:", df)

def call_api(**context):
    response = {"book": "Clean Code", "author": "Robert Martin"}
    context["ti"].xcom_push(key="api_data", value=json.dumps(response))

def process_json(**context):
    data_json = context["ti"].xcom_pull(key="api_data")
    data = json.loads(data_json)
    processed = {"title": data["book"].upper(), "author": data["author"]}
    context["ti"].xcom_push(key="processed_data", value=json.dumps(processed))

def save_to_db(**context):
    final_json = context["ti"].xcom_pull(key="processed_data")
    print("Saving to DB:", final_json)

def check_nulls(**context):
    print("Null check completed")

def check_duplicates(**context):
    print("Duplicate check completed")

with DAG(
    dag_id="multi_pipeline_final_dag",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
):

    extract = PythonOperator(task_id="extract", python_callable=extract_data)
    transform = PythonOperator(task_id="transform", python_callable=transform_data)
    load = PythonOperator(task_id="load", python_callable=load_data)

    api_task = PythonOperator(task_id="call_api", python_callable=call_api)
    process = PythonOperator(task_id="process_json", python_callable=process_json)
    save = PythonOperator(task_id="save_to_db", python_callable=save_to_db)

    null_check = PythonOperator(task_id="null_check", python_callable=check_nulls)
    dup_check = PythonOperator(task_id="dup_check", python_callable=check_duplicates)

    extract >> transform >> load
    api_task >> process >> save
    null_check >> dup_check
