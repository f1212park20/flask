from flask import Flask, render_template
import pymysql

app = Flask(__name__)

def get_connection():
    connection = pymysql.connect(
        host='my-mysql',  # MySQL 컨테이너 포트로 연결
        user='flaskuser',
        password='flaskpass',
        database='testdb',
        port=3306
    )
    return connection

@app.route("/")
def home():
    conn=get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users;")
            users = cursor.fetchall()  # 결과 가져오기

    finally:
        conn.close()
    return render_template("index.html", users=users)

