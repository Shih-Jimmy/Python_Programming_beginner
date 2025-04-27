score = int(input("please input the score:"))
if score < 0 or score > 100:
    print("Sorry,I can't answer your question.")
elif score >= 90:
    print("Grade A")
elif score >= 80 and score < 90:
    print("Grade B")
elif score >= 70 and score < 80:
    print("Grade C")
elif score >= 60 and score < 70:
    print("Grade D")
else:
    print("Grade E")
