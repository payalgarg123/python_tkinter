from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
#creating new webpage in same website or local host
@app.route("/payal2")
def payal2():
    return render_template("bootstarp1.html")
app.run(debug=True)


