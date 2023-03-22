import requests
from flask import Flask, render_template, request,redirect
import psycopg2

app = Flask(__name__)
#set FLASK_RUN_PORT=8000
conn = psycopg2.connect(database="service_db",
                        user="it_user_l45",
                        password="12345678",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            if len(username) == 0 :
                return render_template('login.html', error="empty login")
            password = request.form.get('password')
            if len(password) == 0 :
                return render_template('login.html', error="empty password")
            cursor.execute("SELECT * FROM service_it.users WHERE login=%s AND password=%s", (str(username), str(password)))
            records = list(cursor.fetchall())
            if len(records) == 0 :
                return render_template('login.html', error="no such user")
            return render_template('account.html', full_name=records[0][1], login=records[0][2],password=records[0][3])
        elif request.form.get("registration"):
            return redirect("/registration/")

    return render_template('login.html')

@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = str(request.form.get('name'))
        if len(name) == 0 :
            return render_template('registration.html', error="empty name")
        login = str(request.form.get('login'))
        if len(login) == 0 :
            return render_template('registration.html', error="empty login")
        password = str(request.form.get('password'))
        if len(password) == 0 :
            return render_template('registration.html', error="empty password")
        cursor.execute('INSERT INTO service_it.users (full_name, login, password) VALUES (%s, %s, %s);',
                       (str(name), str(login), str(password)))
        conn.commit()

        return redirect('/login/')

    return render_template('registration.html')
           
"""
@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    if len(username) == 0 :
        return render_template('login.html', error="empty login")
    password = request.form.get('password')
    if len(password) == 0 :
        return render_template('login.html', error="empty password")
    cursor.execute("SELECT * FROM service_it.users WHERE login=%s AND password=%s", (str(username), str(password)))
    records = list(cursor.fetchall())
    if len(records) == 0 :
        return render_template('login.html', error="no such user")
    return render_template('account.html', full_name=records[0][1], login=records[0][2],password=records[0][3])
"""
