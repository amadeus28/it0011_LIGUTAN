lname = input("Enter last name: ")
fname = input("Enter first name: ")
age = (input("Enter age: "))
contact = input("Enter contact number: ")
course = input("Enter course: ")

f=open("C:\studentinfo.txt", "a")
f.write("Last Name: "+ lname+
         "First Name: "+ fname+
         "Age: "+ age+
         "Contact Number: "+ contact+
         "Course: "+ course)
f.close()
print("Student information has been saved to \'studentinfo.txt\'")