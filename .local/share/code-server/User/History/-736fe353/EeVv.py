ds = open('What_Is_data_science.txt', 'r')

words = ds.read().strip().split(' ')



punctuation = ['!', ',', '.']

cache = {}
for word in words:
    for char in punctuation:
        word = words.replace(punctuation[char],'')
    word = word.lower()
    print(word)

    '''
    if word in cache:
        cache[:1] += 1
    else:
        cache.keys(word)
        cache.items(1)
        '''