# ==========================================
# SALES ANALYSIS PROJECT
# MAIN PROGRAM
# ==========================================


from analysis import (
    get_total_sales,
    get_monthly_sales,
    get_product_sales,
    get_category_sales,
    get_salesperson_sales,
    get_top_customers,
    get_city_sales,
    get_profit_analysis
)




# ------------------------------------------
# Display Overall Sales
# ------------------------------------------


def display_total_sales():


    data = get_total_sales()


    print("\n" + "=" * 60)
    print("              OVERALL SALES SUMMARY")
    print("=" * 60)


    print(data.to_string(index=False))




# ------------------------------------------
# Display Monthly Sales
# ------------------------------------------


def display_monthly_sales():


    data = get_monthly_sales()


    print("\n" + "=" * 60)
    print("                 MONTHLY SALES")
    print("=" * 60)


    print(data.to_string(index=False))




# ------------------------------------------
# Display Top Products
# ------------------------------------------


def display_top_products():


    data = get_product_sales().head(10)


    print("\n" + "=" * 60)
    print("                 TOP 10 PRODUCTS")
    print("=" * 60)


    print(data.to_string(index=False))




# ------------------------------------------
# Display Category Sales
# ------------------------------------------


def display_category_sales():


    data = get_category_sales()


    print("\n" + "=" * 60)
    print("                 CATEGORY SALES")
    print("=" * 60)


    print(data.to_string(index=False))




# ------------------------------------------
# Display Salesperson Performance
# ------------------------------------------


def display_salesperson_performance():


    data = get_salesperson_sales().head(10)


    print("\n" + "=" * 60)
    print("          TOP 10 SALESPERSONS BY SALES")
    print("=" * 60)


    print(data.to_string(index=False))




# ------------------------------------------
# Display Top Customers
# ------------------------------------------


def display_top_customers():


    data = get_top_customers()


    print("\n" + "=" * 60)
    print("                 TOP CUSTOMERS")
    print("=" * 60)


    print(data.to_string(index=False))




# ------------------------------------------
# Display City Sales
# ------------------------------------------


def display_city_sales():


    data = get_city_sales()


    print("\n" + "=" * 60)
    print("                    CITY SALES")
    print("=" * 60)


    print(data.to_string(index=False))




# ------------------------------------------
# Display Profit Analysis
# ------------------------------------------


def display_profit_analysis():


    data = get_profit_analysis().head(10)


    print("\n" + "=" * 60)
    print("             TOP 10 PRODUCTS BY PROFIT")
    print("=" * 60)


    print(data.to_string(index=False))




# ------------------------------------------
# Main Function
# ------------------------------------------


def main():


    print("\n")
    print("=" * 60)
    print("              SALES ANALYSIS PROJECT")
    print("=" * 60)


    display_total_sales()
    display_monthly_sales()
    display_top_products()
    display_category_sales()
    display_salesperson_performance()
    display_top_customers()
    display_city_sales()
    display_profit_analysis()


    print("\n")
    print("=" * 60)
    print("              ANALYSIS COMPLETED")
    print("=" * 60)




# ------------------------------------------
# Run the program
# ------------------------------------------


if __name__ == "__main__":
    main()

