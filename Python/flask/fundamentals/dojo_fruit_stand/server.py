from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    s_id = request.form['student_id']
    full_name = first_name +''+ last_name
    s_count = request.form['strawberry']
    r_count = request.form['raspberry']
    a_count = request.form['apple']
    number = int(s_count) + int(r_count) + int(a_count)
    print(f"Charging {full_name} for {number} fruits.")
    print(request.form)
    return render_template("checkout.html", number = number, first_name = first_name, last_name = last_name, full_name = full_name, s_id = s_id, s_count = s_count, a_count = a_count, r_count = r_count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True, port=5001)    