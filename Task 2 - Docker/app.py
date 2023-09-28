from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('iris_model.pkl')

@app.route('/')
def home():
    return 'Iris Classification API'

@app.route('/predict', methods=['POST','GET'])
def predict():
    try:
        features = [1.1,0.1,2.2,0.5]
        prediction = model.predict([features])[0]
        target_names = ['setosa', 'versicolor', 'virginica']
        result = {'prediction': target_names[prediction]}
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)