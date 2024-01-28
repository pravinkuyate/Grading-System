from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    # Read CSV file
    data = pd.read_csv('Dummy_dataset(1).csv')

    # Pass data to the template
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
