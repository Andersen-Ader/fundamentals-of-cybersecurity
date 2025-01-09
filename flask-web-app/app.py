from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data", methods=['post'])
def data():
    name = request.form['name']
    number = request.form['number']
    return render_template("data.html", name=name, number=number)

if __name__ == '__main__':
    app.run()
