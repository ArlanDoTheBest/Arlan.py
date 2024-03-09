def gen_numbers(n):
    for i in range(n,-1,-1):
        yield i

n = int(input())
gen = gen_numbers(n)

print(*gen)