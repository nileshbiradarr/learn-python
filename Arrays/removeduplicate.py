num = int(input("enter the size of array = "))
array = []

for x in range (num):
    array_item= int(input("enter array item = "))
    array.append(array_item)
    
print(array)

for i in range (0,len(array)):
    print("index i=",i)
    
    
    for j in range (1,len(array)):
        print("index j=",j)
        
        if j<len(array):
                if array[i]==array[j]:
                    array.pop(j)
                    
                
                    print("pop")
                    print("pop j = ",j)
                elif array.pop(j):
                    j-=1
                    
                    print(array)
                     
        

print(array)
                
            
        
    
    