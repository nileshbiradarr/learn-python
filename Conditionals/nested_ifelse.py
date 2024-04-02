name = input("enter the name = ") 
percentage = int(input("enter the percentage = "))

c=[name, percentage]

if percentage>35:
    if percentage<45:
        print("c grade")
    else:
        if percentage<60:
            print("b grade")
        else:
            if percentage<80:
                print("a grade")
            else:
                if percentage<100:
                    print("a++ grade mast ekdam 100 percentage...  congrats bro!!")
else:
    print("fail ho gaya bhai tu rehnede.. ")        




