Trade Data Analysis & Pipeline

This project focuses on preparing and analyzing trade shipment records to make the data suitable for reporting and decision-making. The workflow begins with importing raw trade files and continues through several transformation steps to improve data quality and structure.

Technologies Used:
Python – data loading, cleaning, parsing, feature engineering
Pandas – dataframe manipulation and transformations
SQL – structured storage and querying
Power BI – dashboards and visual analytics

In this project, I worked on building a simple data-cleaning and preparation workflow for trade data. The main goal was to take raw Excel files and convert them into a clean and structured format that can be used for analysis.

I started by loading the raw dataset and identifying issues such as inconsistent column names, mixed number formats, and unstructured product descriptions. To fix these, I used basic data-processing tools including Excel and simple database operations. 

Once the data was cleaned and enriched, I exported the final dataset to a CSV file and stored it in an SQLite database for structured querying. These processed outputs can now be easily connected to tools like Power BI for visualization.

The Trade Data Analysis Pipeline converts raw trade shipment data into a cleaned, structured, and enriched dataset suitable for analysis. Although some advanced enhancements are pending, the core solution is complete and provides a solid foundation for analytics, dashboarding, or further automation.