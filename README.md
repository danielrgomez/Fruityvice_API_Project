# Fruityvice_API_Project
The data pulled comes from a public API called: https://www.fruityvice.com, the data returned is in JSON format.
A job is scheduled to run an ETL process via the jupyther notebook in databricks. The extraction of the data is as a JSON request from the web server, 
the transformation of the data uses PySpark to get the multilines from the nutrition field, creates a timestamp for each job ran and drops the nutrition field, 
finally the data is loaded to a table housed in an S3 bucket. The ingestion table is then consumed by a power bi dashboard that is refreshed every time the scheduled process runs.

Dashboard link:
https://dbc-f5c24415-4f48.cloud.databricks.com/dashboardsv3/01ee8bf319cd1ceeb211511b0d868747/published?o=2891492639599377#

# The Data Set
Fruityvice:
A powerful webservice which provides data for all kinds of fruit! You can use Fruityvice to find out interesting information about fruit and educate yourself. The webservice is completely free to use and contribute to. Understanding the nutritional value of fruits can hlelp individuals make informed choices about their diet, leading to better health and wellness. Moreover, fuits are rich in essential vitamins, minerals and antioxidants which play a major role in prventing chronic diseases as heart disease, strock and certain cancers. The purpose of the dashboard is to help inform users of different types fruits and their nutritional values. 

# Used Tools

## Connect
Uses the requests library in python to get the json request via the fruityvice API. Fruityvice API: https://www.fruityvice.com/api/fruit/all. The json output is then loaded to a variable within the jupyter notebook. 

## Processing
PySpark is used to process the data pulled from the API. A data frame reads the json response from the connection above which includes the following fields: Family, Genus, ID, Name, Nutrition Values, Order. The data frame then extracts each of the nutritional values which are contained within dictionaries these are then added as separate columns within the data frame. The nutritional fields include: Calories, Carbohydrates, Fat, Protein, and Sugar.

## Storage
- Amazon S3

## Visualization
- Power BI
