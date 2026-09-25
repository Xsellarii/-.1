n = int(input())

a = n // 100
b = (n // 10) % 10
c = n % 10

s = a + c

if s > b:
    print(">")
elif s < b:
    print("<")      
else:
    print("=")
