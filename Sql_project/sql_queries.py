# ==========================================
# SQL QUERIES - SALES ANALYSIS PROJECT
# ==========================================


# 1. Overall Sales Summary
TOTAL_SALES_QUERY = """
SELECT
    COUNT(*) AS total_orders,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(quantity * unit_price), 2) AS gross_sales,
    ROUND(
        SUM((quantity * unit_price) * discount / 100),
        2
    ) AS total_discount,
    ROUND(
        SUM(
            (quantity * unit_price)
            - ((quantity * unit_price) * discount / 100)
        ),
        2
    ) AS net_sales
FROM sales
JOIN products
    ON sales.product_id = products.product_id;
"""


# 2. Monthly Sales
MONTHLY_SALES_QUERY = """
SELECT
    DATE_TRUNC('month', sale_date)::DATE AS month,
    COUNT(*) AS total_orders,
    SUM(quantity) AS units_sold,
    ROUND(
        SUM(
            (quantity * unit_price)
            - ((quantity * unit_price) * discount / 100)
        ),
        2
    ) AS net_sales
FROM sales
JOIN products
    ON sales.product_id = products.product_id
GROUP BY DATE_TRUNC('month', sale_date)
ORDER BY month;
"""


# 3. Sales by Product
PRODUCT_SALES_QUERY = """
SELECT
    p.product_name,
    p.category,
    SUM(s.quantity) AS units_sold,
    ROUND(
        SUM(
            (s.quantity * p.unit_price)
            - ((s.quantity * p.unit_price) * s.discount / 100)
        ),
        2
    ) AS net_sales
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY
    p.product_name,
    p.category
ORDER BY net_sales DESC;
"""


# 4. Sales by Category
CATEGORY_SALES_QUERY = """
SELECT
    p.category,
    SUM(s.quantity) AS units_sold,
    ROUND(
        SUM(
            (s.quantity * p.unit_price)
            - ((s.quantity * p.unit_price) * s.discount / 100)
        ),
        2
    ) AS net_sales
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY net_sales DESC;
"""


# 5. Salesperson Performance
SALESPERSON_SALES_QUERY = """
SELECT
    sp.salesperson_name,
    sp.region,
    COUNT(s.sale_id) AS total_orders,
    SUM(s.quantity) AS units_sold,
    ROUND(
        SUM(
            (s.quantity * p.unit_price)
            - ((s.quantity * p.unit_price) * s.discount / 100)
        ),
        2
    ) AS net_sales
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
JOIN salespersons sp
    ON s.salesperson_id = sp.salesperson_id
GROUP BY
    sp.salesperson_name,
    sp.region
ORDER BY net_sales DESC;
"""


# 6. Top Customers
TOP_CUSTOMERS_QUERY = """
SELECT
    c.customer_name,
    c.city,
    c.state,
    COUNT(s.sale_id) AS total_orders,
    SUM(s.quantity) AS units_purchased,
    ROUND(
        SUM(
            (s.quantity * p.unit_price)
            - ((s.quantity * p.unit_price) * s.discount / 100)
        ),
        2
    ) AS total_spent
FROM sales s
JOIN customers c
    ON s.customer_id = c.customer_id
JOIN products p
    ON s.product_id = p.product_id
GROUP BY
    c.customer_name,
    c.city,
    c.state
ORDER BY total_spent DESC
LIMIT 10;
"""


# 7. Sales by City
CITY_SALES_QUERY = """
SELECT
    c.city,
    COUNT(s.sale_id) AS total_orders,
    SUM(s.quantity) AS units_sold,
    ROUND(
        SUM(
            (s.quantity * p.unit_price)
            - ((s.quantity * p.unit_price) * s.discount / 100)
        ),
        2
    ) AS net_sales
FROM sales s
JOIN customers c
    ON s.customer_id = c.customer_id
JOIN products p
    ON s.product_id = p.product_id
GROUP BY c.city
ORDER BY net_sales DESC;
"""


# 8. Profit Analysis
PROFIT_ANALYSIS_QUERY = """
SELECT
    p.product_name,
    p.category,
    SUM(s.quantity) AS units_sold,

    ROUND(
        SUM(
            (s.quantity * p.unit_price)
            - ((s.quantity * p.unit_price) * s.discount / 100)
        ),
        2
    ) AS net_sales,

    ROUND(
        SUM(s.quantity * p.cost_price),
        2
    ) AS total_cost,

    ROUND(
        SUM(
            (s.quantity * p.unit_price)
            - ((s.quantity * p.unit_price) * s.discount / 100)
            - (s.quantity * p.cost_price)
        ),
        2
    ) AS profit

FROM sales s
JOIN products p
    ON s.product_id = p.product_id

GROUP BY
    p.product_name,
    p.category

ORDER BY profit DESC;
"""