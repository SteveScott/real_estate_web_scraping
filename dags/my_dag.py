import datetime as dt
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import  db_insert
import scrape

default_args ={
	'owner': 'airflow',
	'start_date': dt.datetime(2020, 0, 0, 0, 0, 0),
	'concurrency': 1,
	'retries': 0
}

with DAG('my_dag',
			default_args=default_arg,
			schedule_interval='*/1 * * * *',
		) as dag:
	opr_scrape = PythonOperator(task_id='scrape', python_callable=scrape.scrape())
	opr_db_insert = PythonOperator(task_id='db_insert', python_callable=db_insert_df())

opr_scrape >> opr_db_insert


