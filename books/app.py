import sqlite3
# import the Flask class from the flask module
from flask import Flask, render_template, g, request, redirect, url_for

PATH = 'db/data.sqlite'

app = Flask(__name__)

def open_connection():
    connection = getattr(g, '_connection', None)
    if connection == None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection

def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection()
    cursor = connection.execute(sql, values)
    if commit == True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()

    cursor.close()
    return results

@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')  # render a template

@app.route('/history')
def historys():
    historys = execute_sql('SELECT * FROM historys')
    return render_template('history.html', historys=historys)  # render a template

@app.route('/fiction')
def fictions():
    fictions = execute_sql('SELECT * FROM fictions')
    return render_template('fiction.html', fictions=fictions)  # render a template

@app.route('/scienceFiction')
def sciences():
    sciences = execute_sql('SELECT * FROM sciences')
    return render_template('scienceFiction.html', sciences=sciences)  # render a template

if __name__ == '__main__':
    app.run(debug=True)
