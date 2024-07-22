from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, this is a Flask web server!'

if __name__ == '__main__':
    app.run(debug=True)
