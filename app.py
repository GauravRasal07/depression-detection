from jinja2 import Template
from flask import Flask, render_template,request
import numpy as np

app = Flask(__name__)
import pickle
       
@app.route('/')
def index():
    return render_template('index.html', my_title = 'Home')


@app.route('/options')
def options():
    return render_template('options.html', my_title = 'Depression detection - Options')


@app.route('/textual-analysis', methods=['GET', 'POST'])
def text_analysis():
    if request.method == 'POST':
        print("Form values: \n", request.form)
        with open('model','rb') as  f:
                lr = pickle.load(f)

        Age = int(request.form.get('age'))
        Gender= int( request.form.get('gender'))
        Self_employed = int(request.form.get('self_employed'))
        Family_history = int(request.form.get('family_history'))
        Work_interface = int(request.form.get('work_interface'))
        No_employees = int(request.form.get('no_employees'))
        Remote_work = int(request.form.get('remote_work'))
        Tech_company = int(request.form.get('tech_company'))
        Benefits = int(request.form.get('benefits'))
        Care_options = int(request.form.get('care_option'))
        Wellness_Program = int(request.form.get('wellness_program'))
        Seek_help = int(request.form.get('seek_help'))    
        Anonymity = int(request.form.get('anonymity'))     
        Leave = int(request.form.get('leave') )
        Mental_health_consequence = int(request.form.get('mentalhealthconsequence'))
        Phys_health_consequence = int(request.form.get('physhealthconsequence'))
        Coworkers = int(request.form.get('coworkers'))
        Supervisor = int(request.form.get('supervisor'))
        Mental_health_interview = int(request.form.get('mentalhealthinterview'))
        Phys_health_interview =int(request.form.get('physhealthinterview'))
        
        MentalVSPhysical = int(request.form.get('mentalvsphysical'))

        Obs_consequence = int(request.form.get('obs_consequence'))
        
        new_input=np.array([[Age,Gender,Self_employed,Family_history,Work_interface,No_employees,Remote_work,Tech_company,Benefits,Care_options,Wellness_Program,Seek_help,Anonymity,Leave,Mental_health_consequence ,Phys_health_consequence,Coworkers,Supervisor,Mental_health_interview,Phys_health_interview,MentalVSPhysical,Obs_consequence]])
        result =lr.predict(new_input)
        if result==1:
           msg = "you’re suffering from Depression"
        else:
           msg = "You're absolutely fine!"
        return  render_template('result-1.html', prediction = msg, my_title='Result Page')
    
    else:
        return render_template('textual-analysis.html', my_title = 'Textual Analysis')


@app.route('/audio-analysis')
def audio_analysis():
    return render_template('audio-analysis.html', my_title = 'Audio Analysis')


@app.route('/thank-you')
def thank_you():
    return render_template('thank-you.html', my_title = 'Thank You')


@app.route('/suggestions')
def suggestions():
    return render_template('suggestions.html', my_title = 'Suggestions Page')


@app.route('/predict-severity', methods=['GET', 'POST'])
def predict_severity():
    if request.method == 'POST':
        values = []
        for i in range(1, 11):
            values.append(int(request.form.get("que-"+str(i))))
        print("Severity: ", values)
        result = ''
        res = sum(values)
        if res in range(1, 5):
            result = 'Minimal Depression'

        elif res in range(5, 10):
            result = 'Mild Depression'

        elif res in range(10, 15):
            result = 'Moderate Depression'

        elif res in range(15, 20):
            result = 'Moderately Severe Depression'

        elif res >= 20:
            result = 'Severe Depression'

        print("Result: ", result)
        return render_template('result.html', result = result)

    else:
        return render_template('predict-severity.html', my_title = 'Depression detection - Options')




if __name__ == '__main__':
    app.run(debug = True)