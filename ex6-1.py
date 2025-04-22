a = int(input("please input num a:"))
b = int(input("please input num b:"))
c = int(input("please input num c:"))
d = int(input("please input num d:"))
if a>b or c<d or a==c or b<d:
    print("Evolution!")
elif a==b or c>d or a>c or b<d:
    print("Brothers!")
else:
    print("CTBC Brothers is the best!")
