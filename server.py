from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keepthissecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["career-services"] = request.form["career-services"]
    session["experience"] = request.form["experience"]
    session["comment"] = request.form["comment"]
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)