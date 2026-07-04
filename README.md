# Customer Churn Prediction

Predicting customer churn using machine learning to help businesses identify at-risk customers and implement retention strategies.

## Overview

This project builds and compares multiple machine learning models to predict whether a customer will churn (leave) or continue with the business. By identifying customers likely to churn, businesses can proactively engage them with targeted retention strategies.

**Key Features:**
- Comprehensive exploratory data analysis (EDA)
- Data preprocessing and feature engineering
- Multiple ML models trained and evaluated
- Performance comparison and visualization
- Production-ready prediction pipeline

## Project Structure

```
Customer-Churn-Prediction/
│
├── eda.ipynb              # Exploratory Data Analysis
├── models.ipynb           # Model Development & Training
├── main.py                # Production pipeline
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Krish-198/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Exploratory Data Analysis

Open and run the EDA notebook to understand the dataset:
```bash
jupyter notebook eda.ipynb
```

This notebook includes:
- Data loading and overview
- Missing value analysis
- Feature distributions
- Correlation analysis
- Customer segmentation insights

### Model Development

Open the models notebook to see model training and evaluation:
```bash
jupyter notebook models.ipynb
```

Includes:
- Feature preprocessing and encoding
- Train-test split
- Model training (Logistic Regression, Random Forest, Gradient Boosting, etc.)
- Cross-validation and hyperparameter tuning
- Performance metrics and comparison

### Run Predictions

Use the main script for predictions on new data:
```bash
python main.py
```

## Model Performance

The project compares multiple algorithms to identify the best performer:
- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Classifier
- XGBoost
- Support Vector Machine

Performance is evaluated using:
- Accuracy
- Precision & Recall
- F1-Score
- ROC-AUC

## Technologies Used

- **Python 3** – Core language
- **Pandas & NumPy** – Data manipulation
- **Scikit-learn** – ML algorithms
- **XGBoost** – Gradient boosting
- **Matplotlib & Seaborn** – Visualization
- **Jupyter Notebook** – Development environment

## Dataset

The project uses customer data with features including:
- Demographics (age, tenure)
- Service usage patterns
- Contract type and billing information
- Customer service interactions
- Payment methods and charges

**Target Variable:** Churn (binary: Yes/No)

## Results & Insights

Key findings from the analysis:
- Month-to-month contracts have higher churn rates
- Longer tenure correlates with lower churn
- Fiber optic internet customers show different churn patterns
- Service bundling impacts retention

## Future Improvements

- Implement SHAP for model explainability
- Add ensemble stacking models
- Deploy as REST API
- Real-time prediction dashboard
- Incorporate external economic indicators

## Contributing

Contributions are welcome! Feel free to:
- Report issues
- Suggest improvements
- Submit pull requests

## License

This project is open source and available under the MIT License.

## Contact

GitHub: [@Krish-198](https://github.com/Krish-198)

---

Built with passion for machine learning and data science.
