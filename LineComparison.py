
# Load text file
file = open('What_Is_data_science.txt', 'r')

# Strip and split file contents into lines using \n.
lines = file.read().strip().split('\n')

'''
The structure of similarity is:
[rowname_1, rowname_2, shared_words_count]
'''

similarity = []

# This nested for loop compares each line to each other line and counts the identical words between lines.
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        line1 = lines[i].lower()
        line2 = lines[j].lower()

        # If words match, they are added to the set. Ultimately, we take the length of the set.
        shared_words = len(set(line1).intersection(set(line2)))

        # Append result to list of tuples. +1 makes the lines 1-indexed instead of 0-indexed.
        similarity.append((i + 1, j + 1, shared_words))

print(similarity)

# Next we need to sort the lines based on their similarity.
'''
sorted_similarity = sorted(similarity, key=lambda x: x[2], reverse=True)
print(sorted_similarity)
'''


