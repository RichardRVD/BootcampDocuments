from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def success():
    return "Dojo!"

@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def say(name):
    print(name)
    return "Hi, " + name

@app.route('/repeat/<int:num>/<text>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def repeat(num, text):
    print(num)
    print(text)
    return num * str(text)

if __name__=="__main__":
    app.run(debug=True)
