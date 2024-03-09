def even_nums(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i
            
n = int(input("Enter a nonzero and positive number: "))
even = even_nums(n)
print(*even , sep = ' , ')



  

