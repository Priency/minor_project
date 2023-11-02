from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask.json import JSONEncoder

app = Flask(__name__)

# Create a custom JSON encoder that handles int64 values
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.int64):
            return int(obj)
        return super(CustomJSONEncoder, self).default(obj)

app.json_encoder = CustomJSONEncoder  # Set the custom JSON encoder for your Flask app

# Load your trained model from a saved file
with open('../model_2/fake_orofile.pickle', 'rb') as f:
    model = pickle.load(f)

# Define a function for data preprocessing
def preprocess_data(input_data):
    try:
        # Ensure the order of features matches the training data
        features = ['profile_pic', 'name', 'private', '#posts', '#followers', '#follows']

        # Create a dictionary of feature values
        preprocessed_data = {
            feature: input_data[feature]
            for feature in features
        }

        return preprocessed_data
    except Exception as e:
        return None

# Function to predict profiles using your model
def predict_profile(model, input_data):
    try:
        prediction = model.predict([list(input_data.values())])
        return prediction[0]
    except Exception as e:
        return None

@app.route('/')
def welcome():
    return "Welcome to the Fake Profile Detection API"

@app.route('/predict', methods=['POST'])
def predict_fake_profile():
    try:
        data = request.json

        if data is None:
            return jsonify({'error': 'Input data not provided'})

        # Preprocess input data
        preprocessed_data = preprocess_data(data)

        if preprocessed_data is None:
            return jsonify({'error': 'Data preprocessing error'})

        # Use the predict_profile function to make predictions
        prediction = predict_profile(model, preprocessed_data)

        if prediction is None:
            return jsonify({'error': 'Prediction error'})

        # Return the prediction (0 for real, 1 for fake, adjust as needed)
        result = prediction
        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    print("Starting a python server for fake profile detection")
    app.run(debug=True)
