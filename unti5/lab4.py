# Mini Project: Retail sales dashboard using CSV and matplotlib
# Install matplotlib if needed:  pip install matplotlib
import csv, os, random
from collections import defaultdict

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

lakh = FuncFormatter(lambda v, _: f"{v / 1e5:.0f}")

CSV_FILE = "retail_sales.csv"
DASHBOARD_FILE = "sales_dashboard.png"

PRODUCTS = {
    "Laptop": ("Electronics", 55000),
    "Phone": ("Electronics", 20000),
    "Headphones": ("Electronics", 2500),
    "T-Shirt": ("Clothing", 700),
    "Jeans": ("Clothing", 1800),
    "Rice (5kg)": ("Grocery", 450),
    "Notebook": ("Stationery", 60),
}
REGIONS = ["North", "South", "East", "West"]
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def create_sample_csv(rows=300):
    random.seed(42)
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["month", "product", "category", "region", "quantity", "unit_price"])
        for _ in range(rows):
            product = random.choice(list(PRODUCTS))
            category, price = PRODUCTS[product]
            qty = random.randint(1, 5) if price > 10000 else random.randint(1, 30)
            writer.writerow([random.choice(MONTHS), product, category,
                             random.choice(REGIONS), qty, price])
    print(f"Sample data created in '{CSV_FILE}'.")


def load_data():
    data = []
    with open(CSV_FILE, "r", newline="") as f:
        for row in csv.DictReader(f):
            row["quantity"] = int(row["quantity"])
            row["unit_price"] = float(row["unit_price"])
            row["revenue"] = row["quantity"] * row["unit_price"]
            data.append(row)
    return data


def total_by(data, key):
    totals = defaultdict(float)
    for row in data:
        totals[row[key]] += row["revenue"]
    return totals


def print_summary(data):
    total = sum(r["revenue"] for r in data)
    by_product, by_region, by_month = [
        total_by(data, key) for key in ("product", "region", "month")
    ]
    print(f"\n===== SALES SUMMARY =====\nTotal transactions : {len(data)}\n"
          f"Total revenue      : Rs. {total:,.2f}\n"
          f"Best product       : {max(by_product, key=by_product.get)}\n"
          f"Best region        : {max(by_region, key=by_region.get)}\n"
          f"Best month         : {max(by_month, key=by_month.get)}")


def build_dashboard(data):
    by_month, by_product, by_region, by_category = [
        total_by(data, key) for key in ("month", "product", "region", "category")
    ]
    months = [m for m in MONTHS if m in by_month]
    monthly = [by_month[m] for m in months]

    fig, axes = plt.subplots(2, 2, figsize=(14, 9))
    fig.suptitle("Retail Sales Dashboard", fontsize=18, fontweight="bold")

    ax = axes[0][0]
    ax.plot(months, monthly, marker="o", color="tab:blue", linewidth=2)
    ax.set_title("Monthly Revenue Trend")
    ax.set_ylabel("Revenue (Rs. lakh)")
    ax.yaxis.set_major_formatter(lakh)
    ax.grid(True, alpha=0.3)

    ax = axes[0][1]
    products = sorted(by_product, key=by_product.get, reverse=True)
    ax.bar(products, [by_product[p] for p in products], color="tab:green")
    ax.set_title("Revenue by Product")
    ax.set_ylabel("Revenue (Rs. lakh)")
    ax.yaxis.set_major_formatter(lakh)
    ax.tick_params(axis="x", rotation=35)

    ax = axes[1][0]
    wedges, _, _ = ax.pie(
        list(by_category.values()), autopct=lambda p: f"{p:.1f}%" if p >= 3 else "",
        startangle=90, pctdistance=0.75)
    ax.legend(wedges, list(by_category.keys()), title="Category",
              loc="center left", bbox_to_anchor=(0.95, 0.5))
    ax.set_title("Sales Share by Category")

    ax = axes[1][1]
    regions = sorted(by_region, key=by_region.get)
    ax.barh(regions, [by_region[r] for r in regions], color="tab:orange")
    ax.set_title("Revenue by Region")
    ax.set_xlabel("Revenue (Rs. lakh)")
    ax.xaxis.set_major_formatter(lakh)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(DASHBOARD_FILE, dpi=150)
    print(f"Dashboard saved as '{DASHBOARD_FILE}'.")
    plt.show()


if not os.path.exists(CSV_FILE):
    print(f"'{CSV_FILE}' not found.")
    create_sample_csv()

sales_data = load_data()
print_summary(sales_data)
build_dashboard(sales_data)