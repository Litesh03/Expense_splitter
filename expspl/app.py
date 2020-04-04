from flask import Flask, render_template, request, g, jsonify
import sqlite3 as sql
import json

app = Flask(__name__)

@app.before_request
def before_request():
    g.db = sql.connect('database.db')

@app.route('/')
def default_home():
    con = sql.connect('database.db')
    con.execute('CREATE TABLE IF NOT EXISTS monthly_data (Name TEXT, Item TEXT, Date TEXT, Price REAL)')
    print("init............")
    return render_template('index.html')

@app.route('/index.html')
def home():
    con = sql.connect('database.db')
    con.execute('CREATE TABLE IF NOT EXISTS monthly_data (Name TEXT, Item TEXT, Date TEXT, Price REAL)')
    print("init............")
    return render_template('index.html')

@app.route('/members.html')
def members():
    return render_template('members.html')

@app.route('/add.html')
def add():
    return render_template('add.html')

@app.route('/contact.html')
def contacts():
    return render_template('contact.html')

@app.route('/api/v1/storeData',methods=['POST', 'GET'])
def storeData():
    print("inside storedata............")
    if request.method == 'POST':
        print(request)
        incomingData = request.data
        print(incomingData)
        dataDict = json.loads(incomingData)
        print(dataDict)

        try:
            print("try madhe ala")
            name = dataDict['name']
            item = dataDict['item']
            price = dataDict['price']
            date = dataDict['date']

            g.db.execute("INSERT INTO monthly_data (name,item,date,price) VALUES(?,?,?,?)",(name,item,date,price))
            print("store zala")
            g.db.commit()

        except ValueError:
            print('Failed Pushing Data to Database')
            return False

    return jsonify(dataDict)

@app.route('/api/v1.0/get_table',methods=['POST', 'GET'])
def return_expenses():
    # cur = conn.cursor()
    con = sql.connect('database.db')
    cur = con.cursor()
    # cur.execute("SELECT * FROM monthly_data")
    cur.execute("SELECT * FROM monthly_data ORDER BY name")
    # cur.execute("SELECT name FROM monthly_data WHERE name LIKE %mohit%")
    rows = cur.fetchall()
    data = []
    for x in rows:
        data.append({'name':x[0], 'item':x[1], 'price':x[3], 'date':x[2]})
    return jsonify(data)

@app.route('/table.html')
def return_table():
    return render_template("table.html")

def calc_individual_exp():
    con = sql.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT ")

if __name__ == '__main__':
    app.run()