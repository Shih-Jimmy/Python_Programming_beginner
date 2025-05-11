#12. 從鍵盤上輸入10個數，求其平均值。
numbers = []
print("Please input 10 words:")
for i in range(10):
    num = float(input(f"Input {i + 1} number:"))
    numbers.append(num)
average = sum(numbers) / len(numbers)
print(f"The average of these 10 words is:{average}")
