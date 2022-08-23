import mlflow.sklearn
from sklearn.model_selection import train_test_split
import pandas as pd
sk_model = mlflow.sklearn.load_model("mlruns/0/a7600fed5285496aaebe1c16a36fce38/artifacts/model")
csv_url ='http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
try:
    data = pd.read_csv(csv_url, sep=';')
except Exception as e:
    print("Unable to download training & test CSV, check your internet connection. Error: %s", e)
# Split the data into training and test sets. (0.75, 0.25) split.
train, test = train_test_split(data)
# The predicted column is "quality" which is a scalar from [3, 9]
# 6.9 0.45 0.11 2.4 0.043 6.0 12.0 0.99354 3.3 0.65 11.4
tmp = [[0,0,0,0,0,0,0,0,0,0,0]]
#for i in range(11):
#    tmp[0][i]=float(input())
# print(tmp)
test_x = test.drop(["quality"], axis=1)
# print(test_x[:2])
#predictions = sk_model.predict(tmp)
predictions = sk_model.predict(test_x)
print(predictions)