#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )



dictsorted = sorted(filter(lambda item: str(item[1]["salary"]) != 'NaN', data_dict.items()),
                    key = lambda item: item[1]["salary"], reverse = True)

print dictsorted[0][0],"has highest salary of",dictsorted[0][1]["salary"]

for i in range(1,10):
    print dictsorted[i][0], dictsorted[i][1]["salary"], "and", dictsorted[i][1]["bonus"]

data_dict.pop('TOTAL') # remove bad outlier

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


