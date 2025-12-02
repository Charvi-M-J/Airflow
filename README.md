# Airflow

🔹 Overview
This project demonstrates a multi-pipeline workflow orchestrated using Apache Airflow, showcasing how multiple independent data pipelines can run within a single DAG.
It includes end-to-end processes such as ETL (Extract–Transform–Load), API data processing, and data quality validation, using Python functions, XComs, and Airflow task orchestration.
The workflows simulate real-world data engineering scenarios by coordinating ingestion, transformation, and validation tasks in a modular and scalable design.

![image alt]()

📁 Pipeline Overview
1️⃣ ETL Pipeline (Extract → Transform → Load)
Extract sample dataset
Transform data by adding computed columns
Load (print/store) the processed output
2️⃣ API Data Pipeline
Simulate external API call
Process JSON response
Store the cleaned and structured output
3️⃣ Data Quality Pipeline
Perform null-value checks
Run duplicate detection tasks

🔧 Tools & Technologies Used
➤ Apache Airflow (workflow orchestration)
➤ Python (Pandas, JSON handling)
➤ Docker / Local Airflow Setup
➤ Airflow UI (for triggering and monitoring pipelines)

