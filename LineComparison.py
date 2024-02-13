
# Load text file
file = open('What_Is_data_science.txt', 'r')

# Strip and split file contents into lines using \n.
lines = file.read().strip().split('\n')

'''
The structure of similarity is:
[rowname_1, rowname_2, shared_words_count, total_words_count, percent_similarity_score]
'''

similarity = []

'''
This nested for loop compares lines and counts the identical words between lines.
Only the first comparison between lines is made, ie, l1 and l2 but not l2 & l1.
'''

for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        line1 = lines[i].lower()
        line2 = lines[j].lower()

        # Count the total words across both lines
        words_count = len(line1.split()) + len(line2.split())

        # If words match, they are added to the set. We take the length of the set.
        shared_words = len(set(line1).intersection(set(line2)))

        # Calculate percent similarity by comparing identical words to total word count.
        percent_similar = round(shared_words / words_count * 100)

        # Append result to list of tuples. + 1 on lines to make lines 1-indexed.
        similarity.append((i + 1, j + 1, shared_words, words_count, percent_similar))


# Next we need to sort the lines based on their similarity.
sorted_similarity = sorted(similarity, key=lambda x: x[-1], reverse=True)

# Finally, we need a human-readable comparison output.
for elem in sorted_similarity:
    print(f"Line {elem[0]} is {elem[-1]}% like line {elem[1]}. "
        f"There are {elem[2]} matching words and {elem[3]} total words.")

# To view the structure:
# print(sorted_similarity)
