#10. 從鍵盤輸入10個整數，統計其中正數、負數和零的個數，並在螢幕上輸出。
positive_count = 0
negative_count = 0
zero_count = 0
    
print("Please input 10 words:")
for i in range(10):
    num = int(input(f"Input {i + 1} number:"))
    if num > 0:
        positive_count += 1 
    elif num < 0:
        negative_count += 1 
    else:
        zero_count += 1
print(f"The number of positive_count is:",{positive_count})
print(f"The number of negative_count is:",{negative_count})
print(f"The number of zero_count is:",{zero_count})

