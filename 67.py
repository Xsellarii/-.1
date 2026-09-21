a = int(input())
b = int(input())
n = int(input())

total = (a * 100 + b) * n

currency = total // 100
cents = total % 100

print(f"{currency} {cents}")        
