#maximum number from given number

def maximum(x, y):
    if x > y:
        return x
    else:
        return y
    
x=int(input("enter the number x = "))
y=int(input("enter the number Y = "))
print(maximum(x,y))