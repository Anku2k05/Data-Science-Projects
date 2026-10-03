# ==========================================
# SALES VISUALIZATION DASHBOARD
# ==========================================

import matplotlib.pyplot as plt
import seaborn as sns

from analysis import (
    get_monthly_sales,
    get_product_sales,
    get_category_sales,
    get_salesperson_sales,
    get_top_customers,
    get_city_sales,
)


# ==========================================
# DASHBOARD
# ==========================================

def sales_dashboard():

    # --------------------------------------
    # Load Data
    # --------------------------------------

    monthly = get_monthly_sales()
    products = get_product_sales().head(10)
    categories = get_category_sales()
    salespersons = get_salesperson_sales().head(10)
    customers = get_top_customers()
    cities = get_city_sales()

    monthly["month"] = monthly["month"].astype(str)

    # --------------------------------------
    # Overall KPIs
    # --------------------------------------

    total_sales = monthly["net_sales"].sum()
    total_orders = monthly["total_orders"].sum()
    total_units = monthly["units_sold"].sum()

    top_product = products.iloc[0]["product_name"]
    top_city = cities.iloc[0]["city"]

    # --------------------------------------
    # Dashboard Style
    # --------------------------------------

    sns.set_theme(
        style="whitegrid",
        font_scale=0.9
    )

    fig = plt.figure(
        figsize=(18, 15),
        facecolor="#F5F7FA"
    )

    fig.suptitle(
        "SALES ANALYSIS DASHBOARD",
        fontsize=24,
        fontweight="bold",
        y=0.98
    )

    # ======================================
    # KPI CARDS
    # ======================================

    fig.text(
        0.15, 0.925,
        f"₹{total_sales:,.0f}\nTOTAL SALES",
        ha="center",
        va="center",
        fontsize=16,
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.8",
            facecolor="white",
            edgecolor="#D9DEE7"
        )
    )

    fig.text(
        0.38, 0.925,
        f"{total_orders:,}\nTOTAL ORDERS",
        ha="center",
        va="center",
        fontsize=16,
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.8",
            facecolor="white",
            edgecolor="#D9DEE7"
        )
    )

    fig.text(
        0.62, 0.925,
        f"{total_units:,}\nUNITS SOLD",
        ha="center",
        va="center",
        fontsize=16,
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.8",
            facecolor="white",
            edgecolor="#D9DEE7"
        )
    )

    fig.text(
        0.85, 0.925,
        f"{top_product}\nTOP PRODUCT",
        ha="center",
        va="center",
        fontsize=14,
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.8",
            facecolor="white",
            edgecolor="#D9DEE7"
        )
    )

    # ======================================
    # MAIN GRID
    # ======================================

    gs = fig.add_gridspec(
        3,
        2,
        left=0.06,
        right=0.96,
        bottom=0.06,
        top=0.84,
        hspace=0.38,
        wspace=0.25
    )


    # ======================================
    # 1. MONTHLY SALES TREND
    # ======================================

    ax1 = fig.add_subplot(gs[0, 0])

    sns.lineplot(
        data=monthly,
        x="month",
        y="net_sales",
        marker="o",
        linewidth=3,
        markersize=8,
        ax=ax1
    )

    # Fill below line
    ax1.fill_between(
        range(len(monthly)),
        monthly["net_sales"],
        alpha=0.15
    )

    ax1.set_title(
        "Monthly Sales Trend",
        fontsize=14,
        fontweight="bold"
    )

    ax1.set_xlabel("")
    ax1.set_ylabel("Net Sales")

    ax1.tick_params(
        axis="x",
        rotation=30
    )


    # ======================================
    # 2. TOP 10 PRODUCTS
    # ======================================

    ax2 = fig.add_subplot(gs[0, 1])

    products_plot = products.sort_values("net_sales")

    sns.barplot(
        data=products_plot,
        x="net_sales",
        y="product_name",
        hue="product_name",
        legend=False,
        ax=ax2
    )

    ax2.set_title(
        "Top 10 Products by Sales",
        fontsize=14,
        fontweight="bold"
    )

    ax2.set_xlabel("Net Sales")
    ax2.set_ylabel("")

    # Add values
    for container in ax2.containers:
        ax2.bar_label(
            container,
            fmt="%.0f",
            padding=3,
            fontsize=8
        )


    # ======================================
    # 3. CATEGORY DONUT
    # ======================================

    ax3 = fig.add_subplot(gs[1, 0])

    ax3.pie(
        categories["net_sales"],
        labels=categories["category"],
        autopct="%1.1f%%",
        startangle=90,
        wedgeprops=dict(
            width=0.4,
            edgecolor="white"
        )
    )

    ax3.set_title(
        "Sales Distribution by Category",
        fontsize=14,
        fontweight="bold"
    )


    # ======================================
    # 4. SALESPERSON PERFORMANCE
    # ======================================

    ax4 = fig.add_subplot(gs[1, 1])

    salespersons_plot = salespersons.sort_values(
        "net_sales",
        ascending=False
    )

    sns.barplot(
        data=salespersons_plot,
        x="salesperson_name",
        y="net_sales",
        hue="salesperson_name",
        legend=False,
        ax=ax4
    )

    ax4.set_title(
        "Salesperson Performance",
        fontsize=14,
        fontweight="bold"
    )

    ax4.set_xlabel("")
    ax4.set_ylabel("Net Sales")

    ax4.tick_params(
        axis="x",
        rotation=30
    )

    for container in ax4.containers:
        ax4.bar_label(
            container,
            fmt="%.0f",
            padding=3,
            fontsize=8
        )


    # ======================================
    # 5. TOP CUSTOMERS
    # ======================================

    ax5 = fig.add_subplot(gs[2, 0])

    customers_plot = customers.sort_values(
        "total_spent"
    )

    sns.barplot(
        data=customers_plot,
        x="total_spent",
        y="customer_name",
        hue="customer_name",
        legend=False,
        ax=ax5
    )

    ax5.set_title(
        "Top 10 Customers by Spending",
        fontsize=14,
        fontweight="bold"
    )

    ax5.set_xlabel("Total Spent")
    ax5.set_ylabel("")

    for container in ax5.containers:
        ax5.bar_label(
            container,
            fmt="%.0f",
            padding=3,
            fontsize=8
        )


    # ======================================
    # 6. CITY SALES
    # ======================================

    ax6 = fig.add_subplot(gs[2, 1])

    cities_plot = cities.sort_values(
        "net_sales",
        ascending=False
    )

    sns.barplot(
        data=cities_plot,
        x="city",
        y="net_sales",
        hue="city",
        legend=False,
        ax=ax6
    )

    ax6.set_title(
        "Sales by City",
        fontsize=14,
        fontweight="bold"
    )

    ax6.set_xlabel("")
    ax6.set_ylabel("Net Sales")

    ax6.tick_params(
        axis="x",
        rotation=35
    )


    # ======================================
    # FINAL CLEANUP
    # ======================================

    sns.despine()

    plt.show()


# ==========================================
# RUN DASHBOARD
# ==========================================

if __name__ == "__main__":
    sales_dashboard()