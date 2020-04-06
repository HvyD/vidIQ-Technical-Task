#!/usr/bin/env python3

#imports
import sys
import os
import configparser
from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.aws_athena_operator import AWSAthenaOperator
from airflow.operators.s3_file_transform_operator import S3FileTransformOperator
import airflow.hooks.S3_hook
import create_tables
from create_tables import query


#Set Key and pass info from replace items in 'dl.cfg' file
config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID'] = config['AWS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY'] = config['AWS']['AWS_SECRET_ACCESS_KEY']


#Task 2 and 3. Set up partitioned Athena DataBase and move back to S3 buckt. 

class XComEnabledAWSAthenaOperator(AWSAthenaOperator):
    '''
    The Class sets auto path and log for Athen Operator, since it is not native.
    '''
    
    def execute(self, context):
        super(XComEnabledAWSAthenaOperator, self).execute(context)
        # this gets `xcom_push`(ed)
        return self.query_execution_id
    
# database query Dag set to dailey as per requirments
with DAG(dag_id='partitioned_athena_and_S3move',
         schedule_interval ='@dailey',
         start_date=datetime.now()) as partit_dag:

    run_query = XComEnabledAWSAthenaOperator(
        task_id = 'run_query',
        query = query.create_patit_table,
        output_location= config['S3']['OUTPUT_LOCATION'],
        database = config['S3']['DATABASE']
    )
    
    move_results = S3FileTransformOperator(
        task_id = 'move_results',
        source_s3_key = config['S3']['SOURCE_S3_KEY'],
        dest_s3_key = config['S3']['DEST_S3_KEY'],
        transform_script = '/bin/cp'
    )
    
move_results.set_upstream(run_query)

#Set workflow Stream
run_query >> move_results
