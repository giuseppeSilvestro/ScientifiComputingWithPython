# Everything we have done in Networking.py can be done with even less lines of code
# thanks to a library in python called urllib, that creates the socket, encode the
# command and send it for you
import urllib.request, urllib.parse, urllib.error

handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in handle:
    print(line.decode().strip())

# note that there are no headers or footers, just the content of the file

# find the most commond word in the file
handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in handle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

big_count = None
big_word = None
for word, count in counts.items():
    if big_word is None or big_count < count:
        big_word = word
        big_count = count
print('The most common word is "{}", that is repeated {} times'.format(big_word, big_count))
