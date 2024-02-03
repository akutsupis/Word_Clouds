ds = open('What_Is_data_science.txt', 'r')
words = ds.read()
cache = {}
for word in words:
    if word in cache:
        cache[:1] += 1
    else:
        cache.a