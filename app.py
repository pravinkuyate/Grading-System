from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io
import base64
import os
import numpy 
from mpl_toolkits.mplot3d import Axes3D

app = Flask(__name__, static_url_path='/static')


data = pd.read_csv("Dummy_dataset(1).csv")
########################################
import pandas as pd

# Load CSV data


def extract_data(name):
    person_data = data[data['1.Student Name'] == name]
    return person_data.iloc[0]  # Assuming unique names

import matplotlib.pyplot as plt

# Function to plot grading tests
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

def plot_grading_tests(person_data):
    labels = ['Grading Test 1', 'Grading Test 2', 'Grading Test 3']
    marks = person_data[['2.Grading Test 1 marks (1 to 25)', '3.Grading Test 2 marks (1 to 50)', '4.Expected marks in Grading Test 3 (1 to 50)']].tolist()
    plt.figure()  # Create a new figure instance
    colors = ['#FF6EC7', '#7A08FA', '#00FFD1']
    plt.bar(labels, marks,color=colors)

    plt.xlabel('Grading Tests')
    plt.ylabel('Marks')
    plt.title('Grading Test Marks')
    plt.savefig(os.path.join('static', 'grading_tests_plot.png'))  # Save plot as file in static directory
#####################################
def plot_viva(person_data):
    plt.figure(figsize=(12, 6))
    labels = ['viva']
    marks = person_data['5. Viva marks (1 to 30)'].tolist()
    plt.figure()  # Create a new figure instance
    colors = ['#FF6EC7']
    plt.barh(labels, marks,color=colors,height=10)

    plt.xlabel('viva')
    plt.ylabel('Marks')
    plt.title('viva Marks')
    plt.savefig(os.path.join('static', 'plot_viva.png'))
# Function to plot attendance as a pie chart
def plot_attendance(person_data):
    labels = ['Attended', 'Absent']
    attendance = [person_data['6. Total Attendance (%) out of 100'], 100 - person_data['6. Total Attendance (%) out of 100']]
    colors = ['#5EDFFF', '#1597BB'] 
    plt.figure()  # Create a new figure instance
    plt.pie(attendance, labels=labels, autopct='%1.1f%%',colors=colors)
    plt.title('Attendance')
    plt.savefig(os.path.join('static', 'plot_attendance.png'))  # Save plot as file in static directory
##########################################
# Function to plot trainer feedback
# Function to plot trainer feedback
# Function to plot trainer feedback as a pie chart
# Function to plot trainer feedback as a pie chart
# Function to plot trainer feedback
import matplotlib.pyplot as plt
import os

def plot_feedback(person_data):
    labels = ['Poor', 'Good']
    feedback = [person_data['7. Trainer Feedback'], 100 - person_data['7. Trainer Feedback']]
    colors = ['#FFA07A', '#FFDAB9']  # Specify colors for each section

    plt.figure()  # Create a new figure instance
    plt.pie(feedback, labels=labels, autopct='%1.1f%%', colors=colors)
    plt.title('Trainer Feedback')
    plt.savefig(os.path.join('static', 'plot_feedback.png'))
    plt.close()  # Close the figure to free up memory
    return os.path.join('static', 'plot_feedback.png')


# Example usage:
# plot_grading_tests(person_data)
# plot_attendance(person_data)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    
    name = request.form['name']
    person_data = extract_data(name)
    plot_grading_tests(person_data)
    plot_attendance(person_data)
    plot_feedback(person_data)
    plot_viva(person_data)
    return render_template('result.html')




###########################################

# Routes

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Simplified login check: If username and password are not empty, consider it successful
        if username and password:
            return redirect(url_for('search'))  # Redirect to the search route
        
        # If login is unsuccessful, render the login page with an error message
        return render_template('login.html', error_message="Invalid username or password. Please try again.")

    # If it's a GET request, render the login page
    return render_template ('login.html')





@app.route('/navbar')
def navbar():
    # Render the navbar page
    return render_template('navbar.html')


if __name__ == '__main__':
    app.run(debug=True)

