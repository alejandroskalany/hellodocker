from flask import Flask

hellodocker = Flask(__name__)
@hellodocker.route("/")

def run():
    return "\"Hey there docker\""

if __name__ == "__main__":
    hellodocker.run(host="0.0.0.0", port=int("3000"), debug=True)


# to build image
# terminal -- docker build -t username/filename:versioninformation .