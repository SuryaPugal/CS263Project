import pandas
import time
import gc 
from sklearn import linear_model
import math

#profiling
gc.set_debug(gc.DEBUG_STATS)
start_time = time.time()
df = pandas.read_csv("house_training.csv")
X = df[['bedrooms','bathrooms','sqft_living','floors','waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated']]
# X = df[['bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15']]
y = df['price']
regr = linear_model.LinearRegression()
regr.fit(X.values, y)


print("--- %s seconds ---" % (time.time() - start_time))

# Testing accuracy
# correct = 0.0
# total = 0.0
# f = open("house_testing.txt", "r")
# for x in f:
#     values = x.split(',')
#     values = values[2:]
#     values = list(map(float, values))
#     actual = values[0]
#     # print(values)
#     prediction = regr.predict([[values[1],values[2],values[3],values[5],values[6],values[7],values[8],values[9],values[10],values[11],values[12],values[13]]])
#     if actual*1.1 > prediction > .90*actual:
#         correct += 1
#     # else:
#         # print("Incorrect: prediction = ", prediction, "      actual = ",actual)

#     total += 1

# print("Accuracy = ", correct/total)
