import sqlite3
import matplotlib.pyplot as plt
import os
from datetime import datetime

def generate_sales_bar_chart():
    conn = sqlite3.connect("db/ecommerce.db")
    cursor = conn.cursor()
    
    query = """
    SELECT item_id, SUM(total_sales) as total
    FROM TotalSales
    GROUP BY item_id
    ORDER BY total DESC
    LIMIT 10;
    """
    
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    
    if not data:
        return None
    
    items, sales = zip(*data)
    
    plt.figure(figsize=(10,5))
    plt.bar(items, sales, color='skyblue')
    plt.title("Top 10 Items by Total Sales")
    plt.xlabel("Item ID")
    plt.ylabel("Total Sales")
    plt.tight_layout()

    # Save plot
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"demo/sales_chart_{timestamp}.png"
    os.makedirs("demo", exist_ok=True)
    plt.savefig(filename)
    plt.close()
    
    return filename
