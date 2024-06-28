import joblib
import os

# Define the paths to the model files
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rf_model_path = os.path.join(BASE_DIR, 'predictor', 'rf_model.joblib')
svm_model_path = os.path.join(BASE_DIR, 'predictor', 'svm_model.joblib')

# Load the models
rf_model = joblib.load(rf_model_path)
svm_model = joblib.load(svm_model_path)

# Check the types to ensure they are loaded correctly
print(f"Random Forest model type: {type(rf_model)}")
print(f"SVM model type: {type(svm_model)}")