vowels = "AEIOUaeiou"
vowel_counter = 0
consonant_counter = 0
space_counter = 0
otherchar_counter = 0

sentence = input("Enter a string: ")
for char in sentence:
    if char.isalpha():
        if char in vowels:
            vowel_counter += 1
        else:
            consonant_counter += 1
    elif char == " ":
        space_counter += 1
    else:
        otherchar_counter += 1

print("Vowels: ",vowel_counter)
print("Consonant: ",consonant_counter)   
print("Space: ",space_counter)   
print("Other characters: ",otherchar_counter)      