#find given string is palindrome or not

def Palindrome(string):
    left_pos = 0
    right_pos = len(string) - 1
    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            print(a + " = is not a palindrome")
            break
        else:  
            left_pos += 1
            right_pos -= 1
            print(a + " = is a Palindrome ")
        break
a = input('enter the string = ')
Palindrome(a)


