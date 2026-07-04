from src.data_preprocessing import preprocess_data
from src.evaluate_models import evaluate_all_models
from src.train_classical import train_classical_models
from src.train_ensembles import train_ensemble_models


print("Step 1: Data Preprocessing")
preprocess_data()

print("\nStep 2: Classical ML")
train_classical_models()

print("\nStep 3: Random Forest")
train_ensemble_models()

print("\nStep 4: Model Evaluation")
evaluate_all_models()

print("\nProject completed")
