
@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    person_data = extract_data(name)
    plot_grading_tests(person_data)
    plot_attendance(person_data)
    plot_feedback(person_data)
    plot_viva(person_data)
    return render_template('result.html')
