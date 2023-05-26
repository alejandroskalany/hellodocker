from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/', methods=['GET','POST'])

def home():
    return render_template('home.html')

@app.route('/surprise', methods=['GET','POST'])

def surprise():
    if request.method == 'POST':
        return render_template('open.html')


#if __name__ == "__main__":
#    app.run(debug=True)

# to build image
# terminal -- docker build -t username/filename:versioninformation .
# to container
# docker container run -d -p 3000:3000 username/filename:versioninfo