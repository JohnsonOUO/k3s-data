import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv
# read the csv file 
cardio_df = pd.read_csv("cardio_train.csv", sep=";")

cardio_df = cardio_df.drop(columns = 'id')

cardio_df['age'] = cardio_df['age']/365
print(type(cardio_df))
cardio_df.to_json("test.json")
#with open('example.csv', 'w') as file:
#    writer = csv.writer(file)
#    writer.write(cardio_df[:1])
#    writer.writerow(cardio_df[1:2])
