```markdown
# Diamond Price Prediction

## Project Overview
The **Diamond Price Prediction** project uses machine learning to predict diamond prices based on features like carat, cut, color, and clarity. The project follows a structured pipeline, from data ingestion and preprocessing to model training and evaluation, ensuring accuracy and scalability.

## Key Learnings
- **Data Ingestion & Preprocessing**: Learn how to load and clean data, handle missing values, and transform features for model training.
- **Model Training**: Train multiple models like Linear Regression, Random Forest, etc., and evaluate their performance.
- **Model Selection**: Learn how to select the best-performing model based on evaluation metrics like R-squared (R2).
- **Prediction Pipeline**: Understand how to save and load the trained model for predicting diamond prices on new data.


## How to Run the Project

1. **Set Up Environment**:
    - Install the required dependencies using `pip install -r requirements.txt`.

2. **Data Ingestion**:
    - The `DataIngestion` class will load the raw data and split it into training and test sets.

3. **Model Training**:
    - The `model_trainer.py` file trains multiple machine learning models, evaluates them, and saves the best-performing model.

4. **Prediction**:
    - load the model after created on running  `model_trainer.py` .

## Technologies Used
- Python
- Scikit-Learn
- Pandas
- Numpy
- Joblib
- XGBoost, LightGBM, CatBoost
- Jupyter Notebooks
