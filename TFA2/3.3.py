lname = input("Enter last name: ")
fname = input("Enter first name: ")
age = (input("Enter age: "))
contact = input("Enter contact number: ")
course = input("Enter course: ")
lines = ("Last Name: "+ lname+
         "First Name: "+ fname+
         "Age: "+ age+
         "Contact Number: "+ contact+
         "Course: "+ course)
f=open("studentinfo.txt", "a")
f.write(lines)
f.close()
print("Student information has been saved to \'studentinfo.txt\'")