# Fruityvice_API_Project
This ETL pipeline extracts JSON-formatted data from the **Fruityvice API**, processing it via a **scheduled job in Databricks** using Jupyter Notebook. The extraction retrieves data from the web server, while **PySpark** transforms it by parsing multi-line nutrition fields, generating timestamps for each run, and dropping unnecessary fields. The processed data is then loaded into an **S3-housed ingestion table**, which feeds a **Power BI dashboard** that refreshes with each scheduled execution.


# The Data Set
Fruityvice:
Fruityvice is a free web service providing comprehensive nutritional data on various fruits, empowering users to make informed dietary choices for improved health and wellness. With rich insights into essential vitamins, minerals, and antioxidants, Fruityvice helps highlight the role of fruits in preventing chronic diseases such as heart disease, strokes, and certain cancers. The accompanying dashboard enhances user experience by presenting key nutritional values, making fruit selection both educational and impactful.


# Used Tools

## Connect
Uses the requests library in python to get the json request via the fruityvice API. Fruityvice API: https://www.fruityvice.com/api/fruit/all. The json output is then loaded to a variable within the jupyter notebook. A workflow is set up to request the data from the fruityvice API on a scheduled cadence, it runs on a daily basis to update the ingestion table.

## Processing
PySpark is used to process the data pulled from the API. A data frame reads the json response from the connection above which includes the following fields: Family, Genus, ID, Name, Nutrition Values, Order. The data frame then extracts each of the nutritional values which are contained within dictionaries these are then added as separate columns within the data frame. The nutritional fields include: Calories, Carbohydrates, Fat, Protein, Sugar and a TimeStamp field is also created. The data is then saved as a table in Databricks. The data is also pulled into a Warehouse for analytic purposes.

## Storage
The data is then stored in an Amazon S3 bucket which is connected via Databricks.

## Visualization
Power Bi is connected to the warehouse via an API which displays the data using a dashboard with charts and graphs. The dashboard illustrates how each fruit stacks up to the others in terms of their nutritional value. Moreover, it allows the user to interact with the charts and graphs in order to allow the user to get a better understanding of each one of the fruits. 
