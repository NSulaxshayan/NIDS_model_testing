# Import necessary libraries
from flask import Flask, request, render_template, jsonify
import numpy as np
from tensorflow.keras.models import load_model

# Initialize Flask app
app = Flask(__name__)

# Load the saved model
model = load_model('hybrid_ann_model_3.h5')

# Define a route to render the form for feature input
@app.route('/')
def home():
    return render_template('index.html')

# Define a route to handle form submission and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get feature values from the form
        feature_values = {
            'IN_BYTES': float(request.form['IN_BYTES']),
            'IN_PKTS': float(request.form['IN_PKTS']),
            'OUT_BYTES': float(request.form['OUT_BYTES']),
            'MIN_TTL': float(request.form['MIN_TTL']),
            'MAX_TTL': float(request.form['MAX_TTL']),
            'TCP_WIN_MAX_IN': float(request.form['TCP_WIN_MAX_IN']),
            'TCP_WIN_MAX_OUT': float(request.form['TCP_WIN_MAX_OUT']),
            'FLOW_DURATION_MILLISECONDS': float(request.form['FLOW_DURATION_MILLISECONDS']),
            'DURATION_IN': float(request.form['DURATION_IN']),
            'DURATION_OUT': float(request.form['DURATION_OUT']),
            'DST_TO_SRC_SECOND_BYTES': float(request.form['DST_TO_SRC_SECOND_BYTES']),
            'RETRANSMITTED_OUT_BYTES': float(request.form['RETRANSMITTED_OUT_BYTES'])
        }

        # Convert feature values to a list in the correct order
        features = list(feature_values.values())
        
        # Convert features to numpy array and reshape
        features_array = np.array(features).reshape(1, -1)
        
        # Make prediction using the loaded model
        prediction = model.predict([features_array, features_array])
        
        # Determine the predicted class
        predicted_class = 'Attack_DoS' if prediction[0][1] > prediction[0][0] else 'Attack_Benign'
        
        # Pass the predicted class to the template
        return render_template('prediction.html', prediction=predicted_class)
    
    except Exception as e:
        # Handle errors gracefully
        return jsonify({'error': str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
