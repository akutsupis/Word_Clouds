ds = open('What_Is_data_science.txt', 'r')

words = ds.read().split(' ')

punctuation = ['!', ',', '.']
cache = {}
for word in words:
    print(word.lower())

    '''
    if word in cache:
        cache[:1] += 1
    else:
        cache.keys(word)
        cache.items(1)
        '''