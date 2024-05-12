a=int(input("enter the a number = "))
b=int(input("enter the a number = "))

try:
    c = a/b
    print(c)
except:
    print("Error: Denominator cannot be 0.")

# Output: Error: Denominator cannot be 0. 