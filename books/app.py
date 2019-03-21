# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/index')
def index():
    return render_template('index.html')  # render a template

@app.route('/history')
def history():
    return render_template('history.html')  # render a template

@app.route('/fiction')
def fiction():
    return render_template('fiction.html')  # render a template

@app.route('/scienceFiction')
def scienceFiction():
    return render_template('scienceFiction.html')  # render a template

@app.route('/sF1')
def sF1():
    return render_template('sF1.html')  # render a template



# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
