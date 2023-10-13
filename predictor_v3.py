'''
This Predictor is using {{decision Tree Algorithm }}
'''

#   1. Ask User TO Enter Date..!
date :str = input('Enter Date : DD MM YYYY :: ')

#   2. DATA cleaning -> fetching out DAY and MONTH from date
import Day_Date
month_name = Day_Date.monthAtDate(date=date)
day_number = Day_Date.dayAtDate(date=date) + 1 # +1 because daying starts from 1 in sheet

'''if on given date there is holiday or not cheking..! '''
if day_number != 7:
    flag = input(f"Is holoday on this date {date} ? Yes/No :: ")

    if flag == 'Yes' or 'yes' or 'y':
        day_number += 7
# print(day_number)

#   3. Reading DATA files.!
import pandas as pd
area_name = input("Enter Area name:: ")
area_name = ('').join(list(area_name))
xl_file = pd.ExcelFile(f'DATA\{area_name}.xlsx')
#   Datasheet fetched..!

data_sheet = pd.read_excel(xl_file,month_name)

graph_data = data_sheet.drop(['week1','week2','week3','week4','week5','TotalParking_Space'],axis='columns')
#   4. TIme to train the model.!
from sklearn.tree import DecisionTreeRegressor
import math
model = DecisionTreeRegressor(max_depth=3)
model.fit(graph_data.drop(['BookedSlots','Day'],axis='columns'),graph_data.drop(['Day_key','Day'],axis='columns'))

''' 🔴Predict method taked 2d array as input!!!!🔴'''
predicted_value = model.predict([[day_number]])
predicted_value = math.ceil(predicted_value[0])

available_slots = (data_sheet['TotalParking_Space'][0] - predicted_value)/data_sheet['TotalParking_Space'][0] *100
print(f'Probability of Available slots on "{date}" at "{area_name}" area is "{available_slots:.2f}%" . \n THANK YOU .!😏')

#   5. Write Predicted data into file.!
with open('DATA\predicted_data.txt','a') as file:
    file.write(f'\n{available_slots:.2f} --- {Day_Date.DATE()} - {date}')
