from collections import defaultdict
freq = {}   # frequency of words in text
line = "Every once in a while, a new technology, an old problem, and a big idea turn into an innovation"
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
newwords = sorted(words)

for w in newwords:
    print ("%s:%d" % (w,freq[w]))
