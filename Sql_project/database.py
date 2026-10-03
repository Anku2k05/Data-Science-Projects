# Import PostgreSQL connection module
import psycopg2


# Create database connection
def create_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="sales_management",
        user="postgres",
        password="postgres",
        port="5432"
    )

    return connection


# Test database connection
if __name__ == "__main__":
    connection = create_connection()

    print("Database connected successfully")

    connection.close()
