word = input("Enter a word: ")

for i in word:
    if i.lower() in 'aeiou':
        continue  # Skip vowels
    print(i)