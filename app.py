from flask import Flask, render_template
import pandas as pd
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_url_path='/static')

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/navbar')
def signin():
    return render_template('navbar.html')


#def index():
    # Read CSV file
 #   data = pd.read_csv("Dummy_dataset(1).csv")

    # Pass data to the template
  #  return render_template('index.html',data=data)


if __name__ == '__main__':
    app.run(debug=True)

