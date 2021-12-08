input = input("")
letters = list(input)
for i in letters:
    letter_count = {i:letters.count(i) for i in letters}
print(letter_count)
