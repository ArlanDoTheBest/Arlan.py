def has_33(list):
    for i in range(len(list)):
        if(list[i] == 3 and list[i+1] == 3):
            return True
        elif(list[i]==3 and list[i+1] != 3):
            return False

print(has_33([1, 3, 3]))  
print(has_33([1, 3, 1, 3]))      
print(has_33([3, 1, 3]))