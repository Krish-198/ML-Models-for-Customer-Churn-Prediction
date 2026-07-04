[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/Krish-198/Customer-Churn-Prediction?style=social)](https://github.com/Krish-198/Customer-Churn-Prediction)

# Customer Churn Prediction

Predicting customer churn using machine learning to help businesses identify at-risk customers and implement retention strategies.

**Project:** AI Internship for Young Achievers | **Organization:** Corporate Gurukul  
**Institution:** National University of Singapore (NUS) | **Mentor:** Prof. Sanka Rasnayaka

## Overview

This project was developed during the AI Internship for Young Achievers program at NUS under the guidance of Prof. Sanka Rasnayaka through Corporate Gurukul. The goal was to build and compare multiple machine learning models to predict whether a customer will churn (leave) or continue with the business.

By identifying customers likely to churn, businesses can proactively engage them with targeted retention strategies, ultimately improving customer lifetime value and business sustainability.

**Key Features:**
- Comprehensive exploratory data analysis (EDA)
- Data preprocessing and feature engineering
- Multiple ML models trained and evaluated
- Performance comparison and visualization
- Production-ready prediction pipeline
- Real-world business insights and recommendations

## Project Structure

```
Customer-Churn-Prediction/
│
├── notebooks/
│   ├── eda.ipynb              # Exploratory Data Analysis
│   └── models.ipynb           # Model Development & Training
├── src/
│   └── preprocessing.py       # Data preprocessing utilities
├── main.py                    # Production pipeline
├── requirements.txt           # Python dependencies
├── LICENSE                    # MIT License
└── README.md                  # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Jupyter Notebook (for exploring notebooks)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Krish-198/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Exploratory Data Analysis

Open and run the EDA notebook to understand the dataset:
```bash
jupyter notebook notebooks/eda.ipynb
```

This notebook includes:
- Data loading and overview
- Missing value analysis
- Feature distributions and relationships
- Correlation analysis
- Customer segmentation insights
- Visualizations and key findings

### Model Development

Open the models notebook to see model training and evaluation:
```bash
jupyter notebook notebooks/models.ipynb
```

Includes:
- Feature preprocessing and encoding
- Train-test split with stratification
- Model training (Logistic Regression, Random Forest, Gradient Boosting, XGBoost, SVM)
- Cross-validation and hyperparameter tuning
- Performance metrics and comprehensive comparison
- ROC-AUC curves and confusion matrices
- Feature importance analysis

### Run Predictions

Use the main script for predictions on new data:
```bash
python main.py
```

## Model Performance

The project compares multiple algorithms to identify the best performer:

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | 79.2% | 0.81 | 0.65 | 0.72 | 0.85 |
| Random Forest | 82.5% | 0.84 | 0.71 | 0.77 | 0.89 |
| Gradient Boosting | 83.1% | 0.85 | 0.73 | 0.79 | 0.91 |
| XGBoost | 84.2% | 0.86 | 0.75 | 0.80 | 0.92 |
| Support Vector Machine | 80.8% | 0.82 | 0.68 | 0.74 | 0.87 |

**Best Model:** XGBoost with 84.2% accuracy and 0.92 ROC-AUC score

## Technologies Used

- **Python 3** – Core programming language
- **Pandas & NumPy** – Data manipulation and numerical computing
- **Scikit-learn** – Machine learning algorithms and utilities
- **XGBoost** – Gradient boosting implementation
- **Matplotlib & Seaborn** – Data visualization
- **Jupyter Notebook** – Interactive development environment

## Dataset

The project uses customer data with features including:

**Demographics:**
- Age, tenure, senior citizen status
- Monthly charges, total charges

**Service Usage:**
- Internet service type (Fiber, DSL, No internet)
- Phone service, multiple lines
- Online security, backup, device protection
- Streaming TV, streaming movies, tech support

**Contract & Billing:**
- Contract type (Month-to-month, One year, Two year)
- Paperless billing, payment method
- Customer service interactions

**Target Variable:** Churn (binary: Yes/No)

## Key Insights & Findings

From the exploratory analysis and modeling:

1. **Month-to-month contracts** have significantly higher churn rates (42%) compared to 1-year (11%) and 2-year (3%) contracts

2. **Tenure matters:** Customers with longer tenure show dramatically lower churn rates. High risk in first 3 months.

3. **Fiber optic customers** show higher churn (42%) compared to DSL users (26%), suggesting service quality issues

4. **Service bundling impact:** Customers using multiple services (phone, internet, streaming) have lower churn rates

5. **Tech support correlation:** Customers with tech support have 25% lower churn

6. **Payment method:** Customers using electronic checks have highest churn rates (45%)

## Business Recommendations

Based on model insights:

- Focus retention efforts on month-to-month contract customers
- Implement onboarding programs for new customers (first 3 months critical)
- Investigate fiber optic service quality issues
- Incentivize service bundling
- Promote tech support adoption
- Encourage paperless billing and automatic payments

## Future Improvements

- Implement SHAP for advanced model explainability
- Add ensemble stacking models for improved accuracy
- Deploy as REST API for real-time predictions
- Build real-time prediction dashboard with Streamlit
- Incorporate external economic indicators
- Add customer satisfaction survey data
- Develop A/B testing framework for retention strategies
- Implement reinforcement learning for optimal intervention timing

## Project Learning Outcomes

Through this internship project, I learned:

✅ End to end machine learning workflow from data exploration to model deployment  
✅ Best practices in data preprocessing and feature engineering  
✅ Model selection and hyperparameter tuning strategies  
✅ Interpreting business metrics from ML models  
✅ Presenting technical insights to non-technical stakeholders  
✅ Professional code organization and documentation  

## Files & Documentation

- `eda.ipynb` – Complete exploratory data analysis with visualizations
- `models.ipynb` – Model training, evaluation, and comparison
- `main.py` – Production-ready prediction script
- `requirements.txt` – All dependencies with versions
- `LICENSE` – MIT License for open source use

## Contributing

Contributions are welcome! Feel free to:
- Report issues or suggest improvements
- Fork the repository and submit pull requests
- Improve documentation and examples
- Add new features or models

## License

This project is open source and available under the **MIT License**. See LICENSE file for details.

## Acknowledgments

Special thanks to:
- **Prof. Sanka Rasnayaka** – Project mentor and guide at NUS
- **Corporate Gurukul** – Providing this valuable internship opportunity
- **National University of Singapore** – Institution support and resources
- All instructors in the AI Internship for Young Achievers program

