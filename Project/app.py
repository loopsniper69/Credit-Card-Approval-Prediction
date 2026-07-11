from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict")
def predict():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():

    gender = request.form["gender"]
    income = request.form["income"]
    employment = request.form["employment"]
    education = request.form["education"]
    house = request.form["house"]

    print("Gender:", gender)
    print("Income:", income)
    print("Employment:", employment)
    print("Education:", education)
    print("House:", house)

    prediction = "Approved"

    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)