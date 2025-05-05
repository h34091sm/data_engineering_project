The aim of this project is to create an ETL pipeline in which JSON data is extracted, transformed using Python then Loaded into an SQL database.
The version of SQL used for the database and querying is SQLITE

The files/directories used for the pipeline include:
    data_script.py - extracts json data, cleans the data and transforms into CSV format
    sqlite.py - converts CSV data into sql databases 
    output directory - contains CSV files for different entities and includes the database file named 'orders.db' 
    unit_test.py - unit tests for the key functions in the extraction process 
    orders.json directory - input json data
    
Once the final databases have been created, some query files have been provided to extract information from it:
    order_query.sql - extracts information regarding the orders entity
    store_query.sql - extracts information regarding the store entity
    line_item_query.sql - extracts information regarding the line items entity
    billing_query.sql - extracts information regarding the billing details 


In order to run the pipeline and produce the databases, do the following:
    Run the file named 'data_script.py' - eg with the command 'python3 data_script.py'
    Run the file named 'sqlite.py' - eg with the command 'python3 sqlite.py'
    
Once the databases have been created in the 'output' directory, they can be viewed in VSCode (with the relevant extensions) or DB Browser (see https://sqlitebrowser.org/). The queries can then be run.

To display the relationship between different entities, an Entity Relationship Diagram included in the root directory with the name 'EntityRelationshipDiagram.pdf'.