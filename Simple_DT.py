import matplotlib 
import sys
matplotlib.use('Agg')
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

import matplotlib.pyplot as plt

import pandas as pd
df = pd.read_csv("Sample_Data.csv")
#print(data.head())

# Lets Try converting to numerical due to known reasons

d = {"UK": 0, "USA" : 1, "N": 2}
df["Nationality"] = df["Nationality"].map(d)

d = {"NO": 0, "YES": 1}

df["Go"] = df["Go"].map(d)
print(df)


# sINCE ALL DATA IS NOW IN NUMERICAL LETS TRY TO...

X = df[["Age","Experience","Rank","Nationality"]]
y = df["Go"]

dtre = DecisionTreeClassifier()

dtre= dtre.fit(X,y)

tree.plot_tree(dtre, feature_names= X.columns)

plt.savefig("decision_tree.png")  # Save as PNG
plt.show()