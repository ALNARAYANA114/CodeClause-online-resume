from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def resume():
    return render_template('resume_form.html')

@app.route('/generate', methods=['POST'])
def generate_resume():
    resume_data = {
        'name': request.form['name'],
        'title': request.form['title'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'summary': request.form['summary'],
        'experience': [],
        'education': []
    }

    for i in range(1, 4):  # Adjust as needed
        exp_title = request.form.get(f'exp_title_{i}')
        exp_company = request.form.get(f'exp_company_{i}')
        exp_year = request.form.get(f'exp_year_{i}')
        exp_description = request.form.get(f'exp_description_{i}')
        if exp_title:
            resume_data['experience'].append({
                'job_title': exp_title,
                'company': exp_company,
                'year': exp_year,
                'description': exp_description
            })

        edu_degree = request.form.get(f'edu_degree_{i}')
        edu_university = request.form.get(f'edu_university_{i}')
        edu_year = request.form.get(f'edu_year_{i}')
        if edu_degree:
            resume_data['education'].append({
                'degree': edu_degree,
                'university': edu_university,
                'year': edu_year
            })

    return render_template('resume.html', resume=resume_data)

if __name__ == '__main__':
    app.run(debug=True)
