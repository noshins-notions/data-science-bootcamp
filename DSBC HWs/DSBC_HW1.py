
# Problem 1
fib = [0,1]

for i in range(7):
    fib = fib + [sum(fib[-2:])]

print(fib)

# Problem 2
print(fib[1::2])

# Problem 3
string = """I have provided this text to provide tips on creating interesting paragraphs.

First, start with a clear topic sentence that introduces the main idea.

Then, support the topic sentence with specific details, examples, and evidence.

Vary the sentence length and structure to keep the reader engaged.

Finally, end with a strong concluding sentence that summarizes the main points.

Remember, practice makes perfect!"""

words = string.lower().strip()

lenWords = len(words)
        
for i in range(lenWords):
    if words[i].isalpha() == False and words[i] != " ":
        words = words.replace(words[i],"!")

words = words.replace("!", " ").split()

unique = [ ]

lenWordsNew = len(words)

for i in range(lenWordsNew):
    if words[i] not in unique:
        unique.append(words[i])

print(unique)
print(len(unique))

# Problem 4

def count_vowels(word):
    vowels = ['a','e','i','o','u']
    count = 0
    for i in range(len(word)):
        if word[i].lower() in vowels:
            count += 1
    return count

print(count_vowels('OUIoui'))

# Problem 5

animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']

for animal in animals:
    print(animal.upper())

# Problem 6

for i in range(1,21):
    if i % 2 == 0:
        print(i,"is even")
    else:
        print(i, "is odd")

# Problem 7

def sum_of_integers(a, b):
    return a + b

print(sum_of_integers(12,124))
