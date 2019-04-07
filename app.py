from flask import *
from databases import *
import databases
app = Flask(__name__)

@app.route('/' , methods = ['GET','POST'])
def home():
    if(request.method == 'GET'):
        return render_template('home.html')
    else:
        Name = request.form['name']
        Age = request.form['age']
        Subject = request.form['subject']
        databases.add_applicant(Name, Age, Subject)
        return render_template("home.html" )

@app.route('/applicants')
def show():
	return render_template('applicants.html',applicants = databases.query_all())

if __name__ == '__main__':
    app.run(debug=True)

