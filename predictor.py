from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

#creat a data frame
dataframe =  pd.read_excel("Predictor\ParkingDataOfRingRoad.xlsx")
# print(dataframe)

#we dont need the totalslots column in prediction.
#so new dataframe for the graph/

graphDataFrame = dataframe.drop(['TotalSolts'],axis='columns')
# print(graphDataFrame)

'''
create a linear model
1. create a instance of the linearRegression model.
'''
linearModel = linear_model.LinearRegression()
linearModel.fit(graphDataFrame.drop(['AvailableSlots'],axis='columns'),graphDataFrame.drop(['Date'],axis='columns'))
# predict() takes 2D array as parameter.!
predicted_value = linearModel.predict([[eval('2023-9-5')]])
print(math.ceil(predicted_value))
'''
Plote a grpah for simple representation using mtlplotlib
1. give lable to each axis.
2. Pass value to each of axis. using scatter()
3. CAll Show() to see graph.
6. plot a line
----Optional----
4. wanna see coeficent? print(model.coef_)
5. wanna see intercept? print(model.intercept_)
'''
# print(type(graphDataFrame.Date[0]))
# print(graphDataFrame.Date[0])
xpoints = np.array([min(graphDataFrame['Date']),eval('2023-9-5')])
ypoints = np.array([min(graphDataFrame['AvailableSlots']),int(predicted_value)])
plt.xlabel("Date")
plt.ylabel("AvailableSlots")
plt.scatter(graphDataFrame['Date'],graphDataFrame['AvailableSlots'],c='red',marker='+')
plt.plot(xpoints,ypoints,color='k')
plt.show()
