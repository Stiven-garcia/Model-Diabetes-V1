from flask import Flask, render_template, request
#import joblib import load

app = Flask(__name__)
#model = load(open("models/model_perceptron.joblib"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    #prediction = model.predict()
    #prediction = 1 if prediction == 1 else -1
    #return render_template("index.html", prediction=prediction)
    return 'hola mundo'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)




