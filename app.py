from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/surprise', methods=['GET','POST'])
def surprise():
    if request.method == 'POST':
        return render_template('open.html')

@app.route('/age', methods=['POST'])
def age():
    return render_template('age.html')

@app.route('/ageresult', methods=['POST'])
def ageresult():
    if request.method == 'POST':
        age_input = request.form['age']
        result = float(age_input) / 7
        return render_template('ageresult.html', age_input=age_input, result=result, calculation_success=True)

if __name__ == "__main__":
    app.run(debug=True)

# to build image
# terminal -- docker build -t username/filename:versioninformation .
# to container
# docker container run -d -p 3000:3000 username/filename:versioninfo