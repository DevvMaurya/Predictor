from sklearn.kernel_ridge import KernelRidge
from sklearn import linear_model
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt 
import Day_Date 

''' Create dataframe..!'''
df = pd.read_excel("Predictor\ParkingDataOfRingRoad.xlsx")
# print(df.loc[0]) ------------------> #help to print row..!

''' Data frame for graph..! '''
df_grp = df.drop(['week1','week2','week3','week4','week5','TotalParking_Space'],axis='columns')
# print(df_grp)

'''
See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df['BookedSlots'][idx] = math.ceil(item)
17.6
-> 🔴solve below bug..!
'''
# for idx , item in enumerate(df['BookedSlots'],0):
#     df['BookedSlots'][idx] = math.ceil(item)
#     print(item)
# df['BookedSlots'][0] = 12.12

model = linear_model.LinearRegression()
model.fit(df_grp.drop(['BookedSlots','Day'],axis='columns'),df_grp.drop(['Day_key','Day'],axis='columns'))
date = input("Enter DATE in THIS FORMAT : DD MM YYYY :: ")
dateNumber = Day_Date.dayAtDate(date=date)
predicted_val = model.predict([[dateNumber+1]]) #(e.g. 1 : Tuesday..! , 
#here +1 beacuse number starts from 0 in that module and in my sheet numbering starts from 1 that's why

''' the predict function return numpy.ndarray as output..!
so we can't pass object to the file so we need to fetch the data from the ndarray . 
that's why predicted_val written as " predicted_val[0][0] " cause array is 2D'''

predicted_val = math.ceil(predicted_val[0][0]) 
print(predicted_val) 
# print(predicted_val[0][0]) 

'''Uptill now the linear model is used to predict ... and have to use ramdom model for prediction.!'''
#10-8-23
#Write the predicted data into data file.!
with open('DATA\predicted_data.txt','a')as file:
    file.write(str(predicted_val)+" "+Day_Date.DATE()+"\n")
    pass

'''Let's plot graph..! using matpoltlib'''
#label X and Y respectivly.!
plt.xlabel("Day")
plt.ylabel("BookedSlots")
#give Dataset which will be shown in graph..!
plt.scatter(df_grp['Day'],df_grp['BookedSlots'])
# plt.plot(np.array([0,0]),np.array([max(df_grp['BookedSlots']),int(predicted_val)]))
plt.show()