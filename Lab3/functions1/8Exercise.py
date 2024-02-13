def spy(x):
    zero_cnt=0
    sevens=False
    for i in x:
        if(i==0 and zero_cnt==0):
            zero_cnt+=1
        elif(i==0 and zero_cnt==1):
            zero_cnt+=1
        elif(i==7 and zero_cnt==2):
            sevens=True
            break
    return sevens                
print(spy([1, 2, 4, 0, 0, 7, 5]))
print(spy([1, 0, 2, 4, 0, 5, 7]))  
print(spy([1, 7, 2, 0, 4, 5, 0])) 