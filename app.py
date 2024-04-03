from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/add', methods = ['POST'])
def add():
     
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO flask VALUES(%s,%s)''',(name,age))
        mysql.connection.commit()
        cursor.close()
    return render_template("home.html")
    
@app.route("/data/", methods = ['GET'])
def data():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM flask.flask''')
        data = cursor.fetchall()
        cursor.close()
    return render_template("data.html", data=data)


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )