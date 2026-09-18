sales = [
    {"product_name": "Laptop", "category": "Electronics", "units_sold": 50, "unit_price": 50000},
    {"product_name": "Phone", "category": "Electronics", "units_sold": 20, "unit_price": 20000},
    {"product_name": "Shirt", "category": "Clothing", "units_sold": 30, "unit_price": 1000},
    {"product_name": "Shoes", "category": "Clothing", "units_sold": 15, "unit_price": 2000}
]

# 1. Total Sales
total_sales = 0
for i in sales: 
    total_sales += i["units_sold"] * i["unit_price"]
print("Total Sales: ", total_sales)

# 2. Average Sales 
avg = total_sales / len(sales)
print("Average Sales per Prodcut: ", avg)

# 3. TOp Selling product 
top_product = sales[0]
for i in sales: 
    if i["units_sold"] > top_product["units_sold"]: 
        top_product = i 
print("The top sellong product: ", top_product["product_name"])

# 4. Sales by category
category_sales = {}
for i in sales: 
    category = i['category']
    amt = i["units_sold"] * i["unit_price"]
    if category in category_sales: 
        category_sales[category] += amt 
    else: 
        category_sales[category] = amt 
print("Sales by category: ")
for category in  category_sales: 
    print(category, ':', category_sales[category])
