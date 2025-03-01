file = open('Technical Midterm Exam\\numbers.txt', 'r')
lines = file.readlines()
file.close()

line_number = 1  

for line in lines:
    numbers = line.strip().split(',')
    total = sum(int(num) for num in numbers)
    status = "Palindrome" if str(total) == str(total)[::-1] else "Not a palindrome"
    
    print(f"Line {line_number}: {line.strip()} ({total}) - {status}")
    line_number += 1  
