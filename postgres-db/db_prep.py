import os
import psycopg2
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get database connection details from environment variables
db_host = os.getenv("POSTGRES_HOST", "localhost")
db_port = os.getenv("POSTGRES_PORT", "5432")
db_name = os.getenv("POSTGRES_DB", "diagscale_todo")
db_user = os.getenv("POSTGRES_USER", "postgres")
db_password = os.getenv("POSTGRES_PASSWORD", "")
db_password_file = os.getenv("POSTGRES_PASSWORD_FILE", "")

# Log the environment variables for debugging
logging.info(f"Attempting to read password from file: {db_password_file}")

# Read the password from the file
if os.path.exists(db_password_file):
    try:
        with open(db_password_file, 'r') as file:
            db_password = file.read().strip()
        logging.info(f"Successfully read the password from {db_password_file}")
    except Exception as e:
        logging.error(f"Error occurred while reading the password file: {e}")
else:
    logging.error(f"Password file {db_password_file} does not exist.")
    db_password = None

if not db_password:
    logging.error("No database password found. Exiting.")
    raise ValueError("No database password found.")

# SQL commands to create the schema and table
check_schema_exists_query = """
SELECT schema_name 
FROM information_schema.schemata 
WHERE schema_name = 'todo_schema';
"""
create_schema_query = "CREATE SCHEMA IF NOT EXISTS todo_schema;"
create_table_query = """
CREATE TABLE IF NOT EXISTS todo_schema.todo_list (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE
);
"""

def connect_and_prep_db():
    """Connect to PostgreSQL and create the schema and table."""
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        conn.autocommit = True
        cursor = conn.cursor()
        # Execute the query to create the schema
        logging.info(f"Creating schema: {create_schema_query}")
        cursor.execute(create_schema_query)
        logging.info("Schema creation attempted.")
        
        # Check if schema exists after creation
        logging.info("Checking if schema exists.")
        cursor.execute(check_schema_exists_query)
        schema_exists = cursor.fetchone()
        if schema_exists:
            logging.info("Schema 'todo_schema' exists.")
        else:
            logging.error("Schema 'todo_schema' was not created.")

        # Execute the query to create the table
        logging.info(f"Creating table: {create_table_query}")
        cursor.execute(create_table_query)
        logging.info("Table creation attempted.")

        # Close the cursor and connection
        cursor.close()
        conn.close()

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        # Print the variables for debugging
        logging.error(f"db_host: {db_host}, db_port: {db_port}, db_name: {db_name}, db_user: {db_user}, db_password: {db_password}, db_password_file: {db_password_file}")


if __name__ == "__main__":
    connect_and_prep_db()
