from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("models/model_perceptron.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    age = request.form.get("Age")
    sex = request.form.get("Sex")
    physActivity = request.form.get("PhysActivity")
    fruits = request.form.get("Fruits")
    veggies = request.form.get("Veggies")
    hvyAlcoholConsump = request.form.get("HvyAlcoholConsump")
    smoker = request.form.get("Smoker")
    highBP = request.form.get("HighBP")
    highChol = request.form.get("HighChol")
    bMI = request.form.get("BMI")
    genHlth = request.form.get("GenHlth")
    physHlthad = request.form.get("PhysHlth")
    diffWalk = request.form.get("DiffWalk")
    heartDiseaseorAttack = request.form.get("HeartDiseaseorAttack")
    prediction = model.predict([[age, sex, physActivity, fruits, veggies, hvyAlcoholConsump, smoker, highBP, highChol, bMI, genHlth, physHlthad, diffWalk, heartDiseaseorAttack]])
    return render_template("index.html", predictions = prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)




