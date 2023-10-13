from datetime import datetime
import calendar

# print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
# print(day_name[datetime.now().weekday()])

def DATE()->str:
    return str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

# date = input()

def dayAtDate(date: str)->int:
    try:
        format1 = datetime.strptime(date , "%d %m %Y").weekday()
    except ValueError:
        format1 = datetime.strptime(date , "%d/%m/%Y").weekday()
    return format1

def monthAtDate(date: str)->str:
    try:
        format1 = datetime.strptime(date, "%d %m %Y")
        date_spliting  = date.split(' ')
    except:
        format1 = datetime.strptime(date, "%d/%m/%Y")
        date_spliting  = date.split('/')

    return calendar.month_name[int(date_spliting[1])]

