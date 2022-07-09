from flask import Flask,render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'this is my second secret key ive ever made...'

@app.route('/')
def survey():
    return render_template('index.html')


@app.route('/process', methods=['post'])
def result():
    print("Survey Info")
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comments']=request.form['comments']
    print(request.form)
    return redirect('/process')

@app.route('/process')
def show_result():
    return render_template('process.html')

if __name__=='__main__':
    app.run(debug=True, port=5001)