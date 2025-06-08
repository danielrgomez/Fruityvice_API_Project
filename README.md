# Fruityvice_API_Project
This ETL pipeline extracts JSON-formatted data from the **Fruityvice API**, processing it via a **scheduled job in Databricks** using Jupyter Notebook. The extraction retrieves data from the web server, while **PySpark** transforms it by parsing multi-line nutrition fields, generating timestamps for each run, and dropping unnecessary fields. The processed data is then loaded into an **S3-housed ingestion table**, which feeds a **Power BI dashboard** that refreshes with each scheduled execution.


# The Data Set
Fruityvice:
Fruityvice is a free web service providing comprehensive nutritional data on various fruits, empowering users to make informed dietary choices for improved health and wellness. With rich insights into essential vitamins, minerals, and antioxidants, Fruityvice helps highlight the role of fruits in preventing chronic diseases such as heart disease, strokes, and certain cancers. The accompanying dashboard enhances user experience by presenting key nutritional values, making fruit selection both educational and impactful.


# Used Tools
### **Tools & Workflow Overview**  

#### **Data Ingestion**  
The pipeline utilizes Python’s `requests` library to retrieve JSON-formatted data from the **Fruityvice API** ([link](https://www.fruityvice.com/api/fruit/all)). The response is stored in a variable within **Jupyter Notebook**, where a scheduled workflow automates daily API requests to ensure the ingestion table remains updated with the latest fruit data.  

#### **Processing**  
**PySpark** is employed for efficient data transformation. A DataFrame ingests the JSON response, parsing key fields such as **Family, Genus, ID, Name, Nutrition Values, and Order**. The nested **Nutrition Values** (Calories, Carbohydrates, Fat, Protein, Sugar) are extracted and converted into individual columns. A **timestamp field** is generated to track each ETL run before the processed data is saved as a table in **Databricks** and integrated into a **Warehouse** for analytical use.  

#### **Storage**  
The transformed data is stored in an **Amazon S3 bucket**, seamlessly connected via **Databricks**, ensuring scalable and reliable access for downstream applications.  

#### **Visualization**  
**Power BI** connects to the warehouse via an API, translating raw data into interactive dashboards with charts and graphs. Users can analyze how different fruits compare in terms of nutritional value, leveraging interactive visual elements for deeper insights into dietary trends.  
