def reverse(a):
    rstr1= ' '
    index=len(a)
    while index>0:
         rstr1 += a [index -1]
         index=index-1
    return rstr1
a = (input("enter the string = "))
print(reverse(a))