# Fruityvice_API_Project
The data pulled comes from a public API called: https://www.fruityvice.com, the data returned is in JSON format.
A job is scheduled to run an ETL process via the jupyther notebook in databricks. The extraction of the data is as JSON request from the web server, 
the transformation of the data uses PySpark to get the multilines from the nutrition field, creates a timestamp for each job ran and drops the nutrition field, 
finally the data is loaded to a table housed in an S3 bucket. The ingest table is then consumed by this a power bi dashboard that is refreshed every time the scheduled process runs.

Fruityvice:
A powerful webservice which provides data for all kinds of fruit! You can use Fruityvice to find out interesting information about fruit and educate yourself. The webservice is completely free to use and contribute to.


