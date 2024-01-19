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
        conn = self.pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS vicii_db")
        cursor.execute("USE vicii_db")
        return conn

    def initialize_db(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(16),
                    email VARCHAR(255),
                    elo INT
                )
            """)
            conn.commit()
