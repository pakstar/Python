
import datetime
current_date =datetime.datetime.now()


birth_date = datetime.datetime(2004,5,14)


date_diff = current_date - birth_date
print(date_diff)
if date_diff.days / 365 > 18:
    print("YES")
else:
    print("No")

# year = 1996
# month = 5
# day = 14

# currentYear = 2022
# currentMonth = 9
# currentDay = 23







# age= currentYear - year
# print(age)
# if age >= 18:
#     print("true")
# else:
#     print("false")
