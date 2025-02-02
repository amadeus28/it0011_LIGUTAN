counter = 5
for x in range(1,6):
    for z in range (1, counter):
        print(" ", end="")
    counter-=1
    for y in range (0,x):
        print(y+1, end="")
    print("")
