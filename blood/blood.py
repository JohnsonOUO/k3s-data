import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# read the csv file 
cardio_df = pd.read_csv("cardio_train.csv", sep=";")

print(cardio_df.head())

# Drop id

cardio_df = cardio_df.drop(columns = 'id')

# since the age is given in days, we convert it into years

cardio_df['age'] = cardio_df['age']/365

print(cardio_df.head())

# checking the null values
print(cardio_df.isnull().sum())

# Checking the dataframe information
print(cardio_df.info())

# Statistical summary of the dataframe
print(cardio_df.describe())

#sns.pairplot(cardio_df)

# split the dataframe into target and features
df_target = cardio_df['cardio']
df_features = cardio_df.drop(columns =['cardio'])

print(cardio_df.columns)
print(df_features.shape)
print(df_features.columns)
print(df_features.head())
print(df_target.shape)
print(df_target.head())
print("--------")
#spliting the data in to test and train sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df_features, df_target, test_size = 0.2)

print(X_train.shape)
print(X_train.columns)
print(y_train.shape)
print(y_train.head())
print(X_test.shape)
print(y_test.head())
print("--------")
from xgboost import XGBClassifier

# model = XGBClassifier(learning_rate=0.01, n_estimators=100, objective='binary:logistic')
model = XGBClassifier()

model.fit(X_train, y_train)

# make predictions on test data

predict = model.predict(X_test)

print(predict[:5])
from sklearn.metrics import precision_score, recall_score, accuracy_score

print("Precision = {}".format(precision_score(y_test, predict)))
print("Recall = {}".format(recall_score(y_test, predict)))
print("Accuracy = {}".format(accuracy_score(y_test, predict)))

model.save_model('bst_save_model.json')
model.save_model('bst_save_model.pkl')

# Import mlflow
import mlflow
import mlflow.sklearn

# mlflow.set_tracking_uri("http://10.20.0.109:31499")
mlflow.set_experiment("cardiovascular_disease")
split_rate = 0.3

with mlflow.start_run(run_name="jack-run-3"):
    mlflow.log_param('split_rate', split_rate)
    
    mlflow.log_metric('precision', precision_score(y_test, predict))
    mlflow.log_metric('recall', recall_score(y_test, predict))
    mlflow.log_metric('accuracy', accuracy_score(y_test, predict))
    
    mlflow.sklearn.log_model(model, artifact_path="xgb-model")
