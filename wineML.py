import pandas
import time
import gc 
from sklearn import linear_model
import math

#profiling
gc.set_debug(gc.DEBUG_STATS)
start_time = time.time()
df = pandas.read_csv("winequality-red.csv")
X = df[['FixedAcidity','VolatileAcidity','CitricAcid','ResidualSugar','Alcohol']]
y = df['Quality']
regr = linear_model.LinearRegression()
regr.fit(X.values, y)

print(regr.predict([[7, .7,1.9,.076,9.4]]))
print("--- %s seconds ---" % (time.time() - start_time))

# Testing accuracy
df = pandas.read_csv("winequality-red-training.csv")
X = df[['FixedAcidity','VolatileAcidity','CitricAcid','ResidualSugar','Chlorides','FreeSulfurDioxide','TotalSulfurDioxide','Density','pH','Sulphates','Alcohol']]
y = df['Quality']
regr = linear_model.LinearRegression()
regr.fit(X.values, y)
correct = 0.0
total = 0.0
f = open("winequality-red-testing.txt", "r")
for x in f:
    values = x.split(',')
    values = list(map(float, values))
    prediction = regr.predict([[values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10]]])
    if math.floor(prediction) == int(values[-1]) or math.ceil == int(values[-1]):
        correct += 1
        print("Correct: prediction = ", prediction, "      actual = ",values[-1])
    else:
        print("Incorrect: prediction = ", prediction, "      actual = ",values[-1])
    total += 1

print("Accuracy = ", correct/total)
