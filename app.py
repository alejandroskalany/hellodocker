from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/surprise', methods=['GET','POST'])
def surprise():
    if request.method == 'POST':
        return render_template('open.html')

@app.route('/age', methods=['GET', 'POST'])
def age():
    return render_template('age.html')

@app.route('/dogyears', methods=['GET', 'POST'])
def ageresult():
    ageinput = request.form['age']
    if request.method == 'POST':
        input1 = int(ageinput)
        result = round(float(input1 / 7))
        return render_template(
            'dogyears.html',
            input1=input1,
            result=result,
            calculation_success=True
        )
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)

# to build image
# terminal -- docker build -t username/filename:versioninformation .
# to container
# docker container run -d -p 3000:3000 username/filename:versioninfo