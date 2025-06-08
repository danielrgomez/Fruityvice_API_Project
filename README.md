# Fruityvice_API_Project
The data pulled comes from a public API called: https://www.fruityvice.com, the data returned is in JSON format.
A job is scheduled to run an ETL process via the jupyter notebook in databricks. The extraction of the data is as a JSON request from the web server, 
the transformation of the data uses PySpark to get the multilines from the nutrition field, creates a timestamp for each job ran and drops the nutrition field, 
finally the data is loaded to a table housed in an S3 bucket. The ingestion table is then consumed by a power bi dashboard that is refreshed every time the scheduled process runs.


# The Data Set
Fruityvice:
A powerful webservice which provides data for all kinds of fruit! You can use Fruityvice to find out interesting information about fruit and educate yourself. The webservice is completely free to use and contribute to. Understanding the nutritional value of fruits can hlelp individuals make informed choices about their diet, leading to better health and wellness. Moreover, fuits are rich in essential vitamins, minerals and antioxidants which play a major role in preventing chronic diseases such as heart disease, strokes and certain cancers. The purpose of the dashboard is to help inform users of different types fruits and their nutritional values. 

# Used Tools

## Connect
Uses the requests library in python to get the json request via the fruityvice API. Fruityvice API: https://www.fruityvice.com/api/fruit/all. The json output is then loaded to a variable within the jupyter notebook. A workflow is set up to request the data from the fruityvice API on a scheduled cadence, it runs on a daily basis to update the ingestion table.

## Processing
PySpark is used to process the data pulled from the API. A data frame reads the json response from the connection above which includes the following fields: Family, Genus, ID, Name, Nutrition Values, Order. The data frame then extracts each of the nutritional values which are contained within dictionaries these are then added as separate columns within the data frame. The nutritional fields include: Calories, Carbohydrates, Fat, Protein, Sugar and a TimeStamp field is also created. The data is then saved as a table in Databricks. The data is also pulled into a Warehouse for analytic purposes.

## Storage
The data is then stored in an Amazon S3 bucket which is connected via Databricks.

## Visualization
Power Bi is connected to the warehouse via an API which displays the data using a dashboard with charts and graphs. The dashboard illustrates how each fruit stacks up to the others in terms of their nutritional value. Moreover, it allows the user to interact with the charts and graphs in order to allow the user to get a better understanding of each one of the fruits. 
