day = int(input("please input a num 1-7:"))
match day:
    case 1|2|3|4|5:
        print("Today is a weekday!")
    case 6|7:
        print("Today is at the weekend!")
    case _:
        print("please input num 1-7!!!")
