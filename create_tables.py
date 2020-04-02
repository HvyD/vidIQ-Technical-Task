class query:
    create_patit_table = """
       CREATE EXTERNAL TABLE IF NOT EXISTS Ampiltude ( 
       adid string, 
       amplitude_attribution_ids string, 
       amplitude_event_type string, 
       amplitude_id string,
        city string, 
        client_event_time string, 
        client_upload_time string, 
        country string, 
        device_brand string, 
        device_carrier string, 
        device_family string, 
        device_manufacturer string, 
        device_model string, 
        device_type string, 
        dma string,
        event_id string,
        event_time string,
        event_type string,
        idfa string,
        language string, 
        library string, 
        location_lat string, 
        location_lng string, 
        os_name string, 
        os_version string, 
        paying string, 
        platform string, 
        processed_time: string, 
        region: string, 
        sample_rate string, 
        server_received_time: string, 
        server_upload_time string, 
        start_version string, 
        user_creation_time string, 
        version_name string
    )

    PARTITIONED BY (client_event_time string)
    STORED AS parquet
    ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
    WITH SERDEPROPERTIES (
      'separatorChar' = ',',
      'quoteChar' = '\"',
      'escapeChar' = '\\' )
    LOCATION 's3://vidiqtask/partit/'; 
    """

