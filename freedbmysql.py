import mysql.connector
import datetime

# Database connection details (replace with your actual credentials)
db_config = {
    "host": "sql.freedb.tech",
    "user": "freedb_admin_jalanjalin",
    "password": "AWTnB?Y#f5GYX5s",
    "database": "freedb_jalanjalin",
}

def addGreeting(name, text):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    sql = "INSERT INTO greeting (name, greeting, datetime) VALUES (%s, %s, NOW())"
    cursor.execute(sql, (name, text))
    connection.commit()

    cursor.close()
    connection.close()

    return {"name": name, "greeting": text, "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

def clearGreeting():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    sql = "DELETE FROM greeting"
    cursor.execute(sql)
    connection.commit()

    cursor.close()
    connection.close()

    return {"data": []}

def getAllGreeting():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    sql = "SELECT * FROM greeting ORDER BY datetime DESC"
    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    data = []
    for row in result:
        data.append({"name": row[0], "greeting": row[1], "datetime": row[2].strftime("%Y-%m-%d %H:%M:%S")})

    return {"data": data}
