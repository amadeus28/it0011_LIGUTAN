numbers = 0

sentence = input("Enter a string with numbers: ")

for char in sentence:
    if char.isdigit():
        numbers += int(char)

print("Sum of numbers added in the string: ", numbers)