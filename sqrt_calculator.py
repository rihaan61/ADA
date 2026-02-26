n = float(input("Enter a positive number: "))

low = 0
high = n

while high - low > 0.00001:  
    mid = (low + high) / 2
    if mid * mid <= n:
        low = mid
    else:
        high = mid

print("Square root:", low)
