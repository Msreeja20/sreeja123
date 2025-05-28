text = "welcome to python loops"
vowels = {'a', 'e', 'i', 'o', 'u'}
count = 0

for letter in text:
    if letter in vowels:
        count += 1

print( "vowel count:", count)
