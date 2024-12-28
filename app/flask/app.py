import os
import psycopg2
from flask import Flask
from flask import render_template
from flask import request

print(f"Name is {__name__}")
app = Flask(__name__, template_folder=".")

os.system("ls")

def whale_connect():
    print("========= GOING TO CONNECT TO YOUR DATABASE >:) =========")
    try:
        connection = psycopg2.connect(dbname="users", user="anton", password="123456", host="whale-db")
        print("Connection established!")
        return connection
    except:
        print("Can't connect to database!")
        return None

@app.route('/users')
def list_users():
    connection = whale_connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")

    all_users = cursor.fetchall()

    cursor.close()
    connection.close()
    return render_template("users.html", users=all_users)

@app.route('/flask', methods=["post", "get"])
def user_form():
    message = "Содержимое формы сбросится после отправки."

    if request.method == "POST":
        fio = request.form.get("fio")
        email = request.form.get("email")

        connection = whale_connect()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO users (fio, email) VALUES ('{fio}', '{email}');")

        connection.commit()
        cursor.close()
        connection.close()
        message = "Ваша форма отправлена в базу данных."

    return render_template("flask.html", result_message=message)

@app.route('/dir')
def list_dir():
    TOP_DIR = "/flask"
    files = [i for i in os.listdir(TOP_DIR)]
    
    return render_template("dir.html", files=files)

if __name__ == '__main__':
    print(app.static_folder)
    app.run(debug=True, host="0.0.0.0", port=5000)
