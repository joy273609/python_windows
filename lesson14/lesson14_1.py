from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.j2')

@app.route("/product")
def product():
    return render_template("product.j2")

@app.route("/pricing")
def pricing():
    return render_template("pricing.j2")

@app.route("/faqs")
def faqs():
    return render_template("faqs.j2")

@app.route("/about")
def about():
    return render_template("about.j2")