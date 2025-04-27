year = int(input("please input the year:"))
month = int(input("please input the month:"))
if month == 1 or month ==3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31")
elif month == 2:
    if year % 4 == 0:
        print("29")
    elif year % 4 != 0:
        print("28")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30")
else:
    print("Sorry,I can't answer your question.")
