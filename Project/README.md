<img width="933" height="555" alt="image" src="https://github.com/user-attachments/assets/049861fd-f83b-4f1f-9934-5ea51308d341" /># Credit Card Approval Prediction

## About the Project

This project is a Machine Learning-based Credit Card Approval Prediction System. It predicts whether a customer's credit card application is likely to be approved based on the information provided by the user.

The main aim of this project is to automate the credit card approval process using different machine learning algorithms and provide the prediction through a simple Flask web application.

---

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- HTML
- CSS
- Joblib

---

## Machine Learning Models Used

The following machine learning models were trained and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

Among these, the Random Forest model was selected for prediction.

---

## Dataset

The project uses two datasets:

- application_record.csv
- credit_record.csv

- You can download the dataset using this link - https://drive.google.com/drive/folders/1g_kOdaiKutTYBqW0nZrsmSvrNaV0uRjt?usp=sharing


These datasets contain customer information and credit history used for training the machine learning model.

---

## Project Modules

The project includes the following stages:

- Importing required libraries
- Reading the datasets
- Data cleaning
- Handling missing values
- Exploratory Data Analysis
- Feature Engineering
- Label Encoding
- Model Training
- Model Evaluation
- Saving the trained model
- Building a Flask Web Application

---

## Accuracy

The obtained model accuracies are:

- Logistic Regression : 94.37%
- Decision Tree : 100%
- Random Forest : 100%

---

## Project Structure

```
Creditcarapproval
│
├── dataset
├── static
├── templates
├── app.py
├── model.pkl
├── model_training.py
├── save_model.py
├── data_preprocessing.py
├── label_encoding.py
├── univariate_analysis.py
├── multivariate_analysis.py
└── README.md
```

---

## How to Run the Project

1. Install the required Python libraries.
2. Run the Flask application using:

python app.py

3. Open your browser and visit:

http://127.0.0.1:5000

---

## Conclusion

This project helped in understanding the complete Machine Learning workflow, including data preprocessing, visualization, model training, evaluation, and deployment using Flask. It demonstrates how machine learning can be used to automate the credit card approval process.

---

## Developed By

**BANGARU SANTOSH**
