from flask import Flask, render_template, request ,redirect, url_for

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io
import base64

app = Flask(__name__, static_url_path='/static')

# Load the dataset
data = pd.read_csv("Dummy_dataset(1).csv")

# Function to generate plots for a specific person
def generate_plots(person_name):
    # Filter data for the specified person
    person_data = data[data['1.Student Name'] == person_name]

    if person_data.empty:
        return None, None  # Return None if person not found

    # Generate plots for the person's data
    plots = {}
    for col in person_data.columns:
        if person_data[col].dtype in [np.int64, np.float64]:
            plt.figure(figsize=(8, 6))
            sns.histplot(person_data[col], kde=True)
            plt.title(f'{col} Distribution for {person_name}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            plots[col] = base64.b64encode(img.getvalue()).decode()

    return person_data, plots

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/travel')
def travel():
    return render_template('travel.html')

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Simplified login check: If username and password are not empty, consider it successful
        if username and password:
            return redirect(url_for('navbar'))  # Redirect to the navbar route
        
        # If login is unsuccessful, render the login page with an error message
        return render_template('login.html', error_message="Invalid username or password. Please try again.")

    # If it's a GET request, render the login page
    return render_template('login.html')

@app.route('/navbar')
def navbar():
    # Render the navbar page
    return render_template('navbar.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/navbar')
def navbar():
    return render_template('navbar.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        person_name = request.form['person_name']
        person_data, plots = generate_plots(person_name)
        if person_data is None:
            return render_template('search.html', error_message="Person not found!")
        else:
            person_table = person_data.to_html(index=False)
            return render_template('results.html', person_name=person_name, person_table=person_table, plots=plots)
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
