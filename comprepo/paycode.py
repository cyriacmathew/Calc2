def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    print(f"Processing file: {file['name']}.")
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to create.
    table_id = "poetic-emblem-309702.CompAnalysis.Emp_data"

    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField('Employee_ID', 'STRING'),
            bigquery.SchemaField('New_Title', 'STRING'),
            bigquery.SchemaField('Establishment_Id', 'STRING'),
            bigquery.SchemaField('Leader_Level_1', 'STRING'),
            bigquery.SchemaField('Leader_Level2', 'STRING'),
            bigquery.SchemaField('Leader_level3', 'STRING'),
            bigquery.SchemaField('GRADE', 'STRING'),
            bigquery.SchemaField('SALARY_ADMIN_LAN', 'STRING'),
            bigquery.SchemaField('EEO_Job_Group', 'STRING'),
            bigquery.SchemaField('Gender', 'STRING'),
            bigquery.SchemaField('Ethnicity', 'STRING'),
            bigquery.SchemaField('Level_of_Education', 'STRING'),
            bigquery.SchemaField('AGE', 'STRING'),
            bigquery.SchemaField('Annual_Rt', 'INTEGER')

            ],
            skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
            source_format=bigquery.SourceFormat.CSV,
        )
    uri = "gs://"+ event['bucket'] +"/" + event['name']

    print(uri)

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.

    load_job.result()  # Waits for the job to complete.

    destination_table = client.get_table(table_id)  # Make an API request.
    print("Loaded {} rows.".format(destination_table.num_rows))
    print(event)

def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    print(f"Processing file: {file['name']}.")
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to create.
    table_id = "poetic-emblem-309702.CompAnalysis.Emp_data"

    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField('Employee_ID', 'STRING'),
            bigquery.SchemaField('New_Title', 'STRING'),
            bigquery.SchemaField('Establishment_Id', 'STRING'),
            bigquery.SchemaField('Leader_Level_1', 'STRING'),
            bigquery.SchemaField('Leader_Level2', 'STRING'),
            bigquery.SchemaField('Leader_level3', 'STRING'),
            bigquery.SchemaField('GRADE', 'STRING'),
            bigquery.SchemaField('SALARY_ADMIN_LAN', 'STRING'),
            bigquery.SchemaField('EEO_Job_Group', 'STRING'),
            bigquery.SchemaField('Gender', 'STRING'),
            bigquery.SchemaField('Ethnicity', 'STRING'),
            bigquery.SchemaField('Level_of_Education', 'STRING'),
            bigquery.SchemaField('AGE', 'STRING'),
            bigquery.SchemaField('Annual_Rt', 'INTEGER')

            ],
            skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
            source_format=bigquery.SourceFormat.CSV,
        )
    uri = "gs://"+ event['bucket'] +"/" + event['name']

    print(uri)

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.

    load_job.result()  # Waits for the job to complete.

    destination_table = client.get_table(table_id)  # Make an API request.
    print("Loaded {} rows.".format(destination_table.num_rows))
    print(event)
def add(first_term, second_term):
    return first_term + second_term

def subtract(first_term, second_term):
    return first_term - second_term

