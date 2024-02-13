from itertools import permutations

def all_perm(x):
    
    list_perm = [''.join(p) for p in permutations(x)]
    
    for list_perm in list_perm:
        print(list_perm)

str = str(input())


all_perm(str)