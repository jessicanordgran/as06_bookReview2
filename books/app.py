import sqlite3
# import the Flask class from the flask module
from flask import Flask, render_template, g, request, redirect, url_for

PATH = 'db/data.sqlite'

# create the application object
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


# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/index')
def index():
    return render_template('index.html')  # render a template

@app.route('/history')
def history():
    history = execute_sql('SELECT history.com_histID, history.com_histLN, history.com_histFN, history.com_histTitle, history.com_histDes FROM history')
    return render_template('history.html', history=history)  # render a template

@app.route('/h1')
def h1():
    return render_template('h1.html')  # render a template

@app.route('/h2')
def h2():
    return render_template('h2.html')  # render a template

@app.route('/h3')
def h3():
    return render_template('h3.html')  # render a template

@app.route('/fiction')
def fiction():
    fiction = execute_sql('SELECT fiction.com_ficID, fiction.com_ficLN, fiction.com_ficFN, fiction.com_ficTitle, fiction.com_ficDes FROM fiction')
    return render_template('fiction.html', fiction=fiction)  # render a template

@app.route('/f1')
def f1():
    return render_template('f1.html')  # render a template

@app.route('/f2')
def f2():
    return render_template('f2.html')  # render a template

@app.route('/f3')
def f3():
    return render_template('f3.html')  # render a template


@app.route('/scienceFiction')
def scienceFiction():
        scienceFiction = execute_sql('SELECT scienceFiction.com_scifiID, scienceFiction.com_scifiLN, scienceFiction.com_scifiFN, scienceFiction.com_scifiTitle, scienceFiction.com_scifiDes FROM scienceFiction')
    return render_template('scienceFiction.html', sciencFiction=scienceFiction)  # render a template

@app.route('/sF1')
def sF1():
    return render_template('sF1.html')  # render a template

@app.route('/sF2')
def sF2():
    return render_template('sF2.html')  # render a template

@app.route('/sF3')
def sF3():
    return render_template('sF3.html')  # render a template



# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
