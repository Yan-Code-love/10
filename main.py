from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'hello world'

app.route('hello')
def Hi_guys():
    return '<h1>Hi guys</h1>'

if __name__ == '__main__':
    app.run()