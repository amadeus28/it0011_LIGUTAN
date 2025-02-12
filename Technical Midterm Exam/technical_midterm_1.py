file = open('numbers.txt', 'r')  
lines = file.readlines()
file.close()

for i, line in enumerate(lines, start=1):
    numbers = line.strip().split(',')
    total_sum = sum(int(num) for num in numbers)
    
    palindrome_status = "Palindrome" if str(total_sum) == str(total_sum)[::-1] else "Not a palindrome"

    print(f"Line {i}: {line.strip()} (sum {total_sum}) - {palindrome_status}")
