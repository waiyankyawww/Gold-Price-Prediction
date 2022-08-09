from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open("models/model.pkl", "rb"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    val1 = request.form["price"]
    # val2 = request.form["bathrooms"]
    # val3 = request.form["floors"]
    # val4 = request.form["yr_built"]
    arr = np.array([val1])
    arr = arr.astype(np.float64)
    pred = model.predict([arr])

    return render_template("index.html", data=int(pred))


if __name__ == "__main__":
    app.run(debug=True)
