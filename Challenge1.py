sum = 0 

for i in range(1001):
    
    if i % 3 == 0:
        sum += i
    elif i % 5 == 0:
        sum += i

print(f"Total is {sum}")