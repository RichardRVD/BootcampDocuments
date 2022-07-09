from flask import Flask, render_template,redirect, session, request
app = Flask(__name__)
app.secret_key = 'this is my first secret key ive ever made'

@app.route('/')
def index():
    if 'button_1' not in session:
        session['button_1'] = 0
    session['button_1']+= 1
    return render_template('index.html', button_1 = session['button_1'])

@app.route('/button/<int:button_num>')
def click_button(button_num): #function linked to "Add two visits" button/link in html
    session[f'button_{button_num}'] += 1 #due to page render of +=1, adds value of two when clicked
    return redirect('/')


@app.route('/reset')
def destroy_session(): #function resets the session linked to "reset" button in html template
    session.clear()
    session[f'button_1'] = 0 #sets the count back to one, due to the reload page render
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True, port=5001)