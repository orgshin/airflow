import pendulum

from airflow.sdk import DAG
from airflow.providers.smtp.operators.smtp import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2025, 9, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    send_email_task = EmailOperator(
        task_id='send_email_task',
        conn_id='conn_smtp_gmail',      # Airflow 3.0 실습부터 추가
        to='joohwan54@gmail.com',       
        subject='Airflow 성공메일',
        html_content='Airflow 작업이 완료되었습니다'
    )