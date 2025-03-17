wordsFilteredCounter = 0
wordCounter = 0
excludedWords = ("and", "but", "or", "nor", "for", "so", "yet", "an", "and", "the", "of")
dictWord = {}
lowercaseWords = []
uppercaseWords = []

words = input("Enter a string statement\n:")
wordList = words.split()

for word in wordList:
    if word not in dictWord and word.lower() not in excludedWords:
        dictWord[word] = 0

for word in wordList:
    if word in dictWord:
        dictWord[word] += 1
        wordsFilteredCounter += 1

for word in dictWord:
    if word[0].islower():
        lowercaseWords.append(word)
    else:
        uppercaseWords.append(word)

lowercaseWords.sort()
uppercaseWords.sort()


sortedWords = lowercaseWords + uppercaseWords

print("\n\n")
for word in sortedWords:
    print(word + " " * (10 - len(word)) + " - " , dictWord[word])

print("\nTotal words filtered: ", wordsFilteredCounter)
