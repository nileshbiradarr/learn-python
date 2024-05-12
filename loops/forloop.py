#printing even numbers from given number with for loop

a = int(input("enter the number = "))
if (a%2) == 1:
    a+=1   
for a in range(a,20,2):
    print(a)