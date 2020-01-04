import sys
sys.path.append("..")
sys.path.append("..")
import scrape
import scrape_for_dag
from db_import_for_dag import puller
from db_insert import insert_df

import datetime as dt
from airflow import DAG

from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
	'owner': 'airflow',
	'start_date': dt.datetime(2019,1,4,13,0,0),
	'concurrency':1,
	'retries':0
	}


with DAG('my_dag',
	default_args=default_args,
	schedule_interval='*/10 * * * *',
	) as dag:
	opr_scrape = PythonOperator(task_id='id_scrape', python_callable=scrape_for_dag.scrape)
	opr_insert = PythonOperator(task_id='id_insert', python_callable=puller)
opr_scrape >> opr_insert


