import mysql.connector


####################  Function  return a list of users by companyId ########################
def get_users_by_company_id(companyId):
    # Establish a connection to the MySQL database
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="company"
    )
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Execute the SELECT statement
    query = "SELECT * FROM user WHERE companyId = %s"
    cursor.execute(query, (companyId,))
    
    # Fetch all rows
    rows = cursor.fetchall()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    # Return the result as a list of dictionaries
    users = []
    for row in rows:
        user = {
            "userId": row[0],
            "userName": row[1],
            "email": row[2],
            "mobile": row[3],
            "password": row[4],
            "companyId": row[5]
        }
        users.append(user)
    
    return users

# get_users_by_company_id(1)
# get_users_by_company_id(2)
get_users_by_company_id(3)
