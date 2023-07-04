import mysql.connector
from datetime import datetime, timedelta

def get_recent_orders():
    # Establish a connection to the MySQL database
    conn = mysql.connector.connect(
       host="localhost",
        user="root",
        password="root@123",
        database="order_assig"
    )
    
    # Create object
    cursor = conn.cursor()
     # 7 days ago
    seven_days_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')
    
    query = "SELECT * FROM orders WHERE createdAt >= %s"
    cursor.execute(query, (seven_days_ago,))
    
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    orders = []
    for row in rows:
        order = {
            "orderId": row[0],
            "title": row[1],
            "description": row[2],
            "createdAt": row[3]
        }
        orders.append(order)
    
    return orders

get_recent_orders()