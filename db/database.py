import mysql.connector
# pooling helps manage and reuse database connections more efficiently
from mysql.connector import pooling

class Database:
    def __init__(self):
        self.dbconfig = {
            "host": "localhost",
            "user": "root",
            "password": "dbuserdbuser",
        }
        self.pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="vicii_pool",
                                                                pool_size=10,
                                                               **self.dbconfig)

    def get_connection(self):
        cursor = conn.cursor()
        try:
            conn = self.pool.get_connection()
            cursor = conn.cursor()
            cursor.execute("USE vicii_db")
            return conn
        
        except Exception as e:
            print(e)

    def initialize_db(self):
        conn = self.pool.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS vicii_db")
            cursor.execute("USE vicii_db")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(16),
                    email VARCHAR(255),
                    elo INT
                )
            """)
            conn.commit()
        except Exception as e:
            print(e)

        finally:
            cursor.close()
            conn.close()