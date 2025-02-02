counter = 1
number = 1

while counter < 6:
    x = 0
    while x < number:
        print(number, end="")
        x += 1    
    print("")
    
    if counter < 3:
        number += 2
    else:
        number +=1
    counter += 1