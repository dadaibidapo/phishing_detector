from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import extract_features_from_url
import joblib
import os
import pandas as pd

# Define the paths to the model files
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rf_model_path = os.path.join(BASE_DIR, 'predictor', 'rf_model.joblib')
svm_model_path = os.path.join(BASE_DIR, 'predictor', 'svm_model.joblib')
scaler_path = os.path.join(BASE_DIR, 'predictor', 'scaler.joblib')
mapping = {0: 'legitimate', 1: 'phishing'}

# Load the models
rf_model = joblib.load(rf_model_path)
svm_model = joblib.load(svm_model_path)
scaler = joblib.load(scaler_path)

class PredictView(APIView):
    def post(self, request):
        url = request.data.get('url')
        if not url:
            return Response({'error': 'URL is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        features = extract_features_from_url(url)
        if not features:
            return Response({'error': 'Could not extract features from URL'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        new_data = pd.DataFrame([features])
        feature_values = scaler.transform(new_data)
        # feature_values = list(features.values())
        # Ensure the features are in the correct order
        sample_features = feature_values
        

        rf_prediction = rf_model.predict(sample_features)[0]
        svm_prediction = svm_model.predict(sample_features)[0]

        # Convert np.int64 to int
        rf_prediction = int(rf_prediction)
        
        rf_label = mapping[rf_prediction]
        svm_label = mapping[svm_prediction]
        
        return Response({
            'rf_prediction': rf_label,
            'svm_prediction': svm_label
        })

