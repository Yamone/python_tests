import datetime

print("Check the day of the week by entering year, month and date.")

year = ''
month = None
day = None

def isLeapYear (year):
    if ((year % 4 == 0) and (year % 100  != 0)) or (year % 400 == 0):
        return True
    else: 
        return False

def checkValidDate(d, m, y):
    try:
        d = int(d)
        first = [1, 3, 5, 7, 8, 10 , 12]
        second = [4, 6, 9, 11]
        minDate = 0
        if(m in first):
            return (d > minDate and d < 32) and d or None
        elif(m in second):
            return (d > minDate and d < 31) and d or None
        else:
            maxDate = isLeapYear(y) and 30 or 29
            return (d > minDate and d < maxDate) and d or None
    except Exception:
        return None
    


def checkMonth(m):
    try:
        m = int(m)
        return (m > 0 and m < 13) and m or None
    except Exception:
        return None

    

while len(year) < 4 or not year.isdigit():
    year = input("Please enter year : ")

year = int(year)

while month == None:
    month = checkMonth(input("Please enter month: "))


while day == None:
    day = checkValidDate(input("Please enter day : "), month, year)


x = datetime.datetime(year, month, day)
print(f'{x.strftime("%B")} {x.strftime("%Y")}, {x.strftime("%d")} is {x.strftime("%A")}')

print("Press any key to exist")
x = input("")


