import random

# Load text file
file = open('What_Is_data_science.txt', 'r')

# Record punctuation to remove
punctuation = ['!', ',', '.', '\n']

# Strip and split file contents into "words"
words = file.read().strip().split(' ')

# Create empty structure list.
structure = []

# Create empty word counts dictionary.
word_counts = {}

# Colors for the word cloud. More colors can be added if desired.
colors = ["Blue", "Green", "Red", "Turquoise", "Pink", "Yellow", "Brown", "Purple"]

'''
The structure of "structure" is a list of dictionaries containing:
{'Word': "word", 'Count': "count", 'Color', "Color"}
'''
# For loop to iterate through each word in the document
for index, word in enumerate(words):
    word_count = index + 1
    # For loop to remove punctuation and standardize case for comparison
    for i in word:
        if i in punctuation:
            word = word.replace(i,'')
    word = word.lower()

    # For loop to count occurances of a word and store it in a dictionary
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

    # Use random to randomly choose a color for each word.
    index = random.randint(0, len(colors) - 1)
    colorassign = colors[index]

    # Creates structured output:
    structure.append({"Word": word, "Count": word_counts[word], "Color": colorassign})


# Print structure for viewing.
print(structure)
print(f"There are {word_count} total words")
