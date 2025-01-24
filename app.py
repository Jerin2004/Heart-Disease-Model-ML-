from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('heart_disease_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = int(request.form['age'])
        cp = int(request.form['cp'])
        thalach = int(request.form['thalach'])

        # Prepare the input array
        user_data = np.array([[age, cp, thalach]])
        prediction = model.predict(user_data)

        # Generate the result message
        result = "You have heart disease." if prediction[0] == 1 else "You don't have heart disease."
        return jsonify({'result': result})

    except ValueError as e:
        return jsonify({'result': 'Invalid input. Please enter valid numbers.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
