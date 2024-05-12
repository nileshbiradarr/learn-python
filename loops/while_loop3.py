#finding even numbers between two numbers with while loop

first = int(input("enter the first number = "))
second = int(input("enter the first number = "))

while first<=second:
    if(first%2) == 0:
       print(first)
       first+=1
    else:
        first+=1
       
       