from flask import Flask, redirect, url_for, request, render_template
import psycopg2
from config import host, user, password, db_name

app = Flask(__name__)
def get_db_connection():
    conn = psycopg2.connect(host=host,
                            database=db_name,
                            user=user,
                            password=password)
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "Device";')
    devices = cur.fetchall()
    cur.close()
    conn.close()
    print(devices)
    print(devices[0])
    print(devices[0][0])
    return render_template('index.html', devices=devices)




if __name__ == "__main__":
    app.run(debug=True)