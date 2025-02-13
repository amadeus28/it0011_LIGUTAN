file = open('Technical Midterm Exam\\numbers.txt', 'r')
lines = file.readlines()
file.close()

line_number = 1  

for line in lines:
    numbers = line.strip().split(',')
    total_sum = sum(int(num) for num in numbers)
    palindrome_status = "Palindrome" if str(total_sum) == str(total_sum)[::-1] else "Not a palindrome"
    
    print(f"Line {line_number}: {line.strip()} ({total_sum}) - {palindrome_status}")
    line_number += 1  
