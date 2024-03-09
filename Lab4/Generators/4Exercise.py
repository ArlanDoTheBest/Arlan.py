def squares(a ,b):
    for i in range(a,b+1):
        yield i*i

a = int(input())
b = int(input())
gen = squares(a , b)

for x in gen:
    print(x)