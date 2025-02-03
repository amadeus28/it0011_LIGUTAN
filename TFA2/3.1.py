fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = int(input("Enter your age: "))
fullname = fname +" "+lname
sliced = fullname[0:3]

print("Full Name: ",fullname)
print("Sliced Name: ",sliced)
txt = "Greeting Message: Hello, {}! Welcome. You are {} years old."
print(txt.format(sliced, age))