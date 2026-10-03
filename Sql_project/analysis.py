# ==========================================
# SALES ANALYSIS
# ==========================================


import pandas as pd


from database import create_connection


from sql_queries import (
    TOTAL_SALES_QUERY,
    MONTHLY_SALES_QUERY,
    PRODUCT_SALES_QUERY,
    CATEGORY_SALES_QUERY,
    SALESPERSON_SALES_QUERY,
    TOP_CUSTOMERS_QUERY,
    CITY_SALES_QUERY,
    PROFIT_ANALYSIS_QUERY
)




# ------------------------------------------
# Function to execute SQL query
# ------------------------------------------


def execute_query(query):
    """
    Execute a SQL query and return the result
    as a Pandas DataFrame.
    """


    connection = create_connection()


    try:
        dataframe = pd.read_sql_query(query, connection)
        return dataframe


    finally:
        connection.close()




# ------------------------------------------
# 1. Overall Sales Analysis
# ------------------------------------------


def get_total_sales():
    return execute_query(TOTAL_SALES_QUERY)




# ------------------------------------------
# 2. Monthly Sales Analysis
# ------------------------------------------


def get_monthly_sales():
    return execute_query(MONTHLY_SALES_QUERY)




# ------------------------------------------
# 3. Product Sales Analysis
# ------------------------------------------


def get_product_sales():
    return execute_query(PRODUCT_SALES_QUERY)




# ------------------------------------------
# 4. Category Sales Analysis
# ------------------------------------------


def get_category_sales():
    return execute_query(CATEGORY_SALES_QUERY)




# ------------------------------------------
# 5. Salesperson Analysis
# ------------------------------------------


def get_salesperson_sales():
    return execute_query(SALESPERSON_SALES_QUERY)




# ------------------------------------------
# 6. Top Customers
# ------------------------------------------


def get_top_customers():
    return execute_query(TOP_CUSTOMERS_QUERY)




# ------------------------------------------
# 7. City Sales Analysis
# ------------------------------------------


def get_city_sales():
    return execute_query(CITY_SALES_QUERY)




# ------------------------------------------
# 8. Profit Analysis
# ------------------------------------------


def get_profit_analysis():
    return execute_query(PROFIT_ANALYSIS_QUERY)




# ------------------------------------------
# Test the analysis
# ------------------------------------------


if __name__ == "__main__":


    print("\n========== TOTAL SALES ==========")


    total_sales = get_total_sales()
    print(total_sales)


    print("\n========== MONTHLY SALES ==========")


    monthly_sales = get_monthly_sales()
    print(monthly_sales)


    print("\n========== TOP PRODUCTS ==========")


    product_sales = get_product_sales()
    print(product_sales.head(10))
