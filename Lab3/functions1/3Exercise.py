def solve(numheads, numlegs):
    chickens = 0
    rabbits = 0 
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        chicken_legs = chickens * 2
        rabbit_legs = rabbits * 4
        if (chicken_legs + rabbit_legs == numlegs):
            break 
    return chickens, rabbits
        

chickens, rabbits = solve (35 , 94)
print("Number of chickens:", chickens)
print("Number of rabbits:", rabbits) 