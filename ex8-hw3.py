#30. 用陣列實現以下功能：輸入5個學生成績，而後求出這些成績的平均值並顯示出來。
numbers = []
print("Please input 5 student grades:")
for i in range(5):
    num = float(input(f"Input {i + 1} student grades:"))
    numbers.append(num)
average = sum(numbers) / len(numbers)
print(f"The average of these 5 student grades is:{average}")
