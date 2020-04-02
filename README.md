# vidIQ Technical Assesment

### The task at hand are: 


<b>1.<b/>	Load attached data file to S3 Bucket
<b>2.<b/>	Implement a Partitioned Athena Database creating its schema using python 
<b>3.<b/>	Use Airflow to add new partitions for Daily events
    

# Setup
1. Python3 & Airflow used
2. Dependencies set in requirment file and at imports
4. create aws config
   * create file `dl.cfg`
   * add the following contents (fill the fields)
    ```bash
   [AWS]
    AWS_ACCESS_KEY_ID=
    AWS_SECRET_ACCESS_KEY=


    [S3]
    BUCKET_NAME = 
    OUTPUT_LOCATION = 
    SOURCE_S3_KEY = 
    DEST_S3_KEY = 
    DATABASE = 

   ```
5. Initialize Airflow & Run Webserver
   
    ```
6. Run Scheduler (Open New Terminal Tab)
   ---
 

## Usage
1. Run ELT 
2. Access Airflow UI at your localhost
3. Create Airflow Connections
4. Run dags in Airflow UI


--Alternatively you can just export via cli:
export AIRFLOW_CONN_AWS_DEFAULT="s3://$AWS_CLIENT_ID:$AWS_CLIENT_SECRET@my-bucket?region_name=$AWS_REGION"
export AWS_DEFAULT_REGION=$AWS_REGION
export AWS_ACCESS_KEY_ID=$AWS_CLIENT_ID
export AWS_SECRET_ACCESS_KEY=$AWS_CLIENT_SECRET


# Test
airflow test partitioned_athena_and_S3move <EXECUTION_DATE>
