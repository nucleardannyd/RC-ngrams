from struct import Node, Edge

book = open("the_mysterious_affair_at_styles.txt", 'r')
text = book.read()
words = text.split()
d = {}
for w in words:
    if w not in d.keys():
        d[w] = Node(w)

    else:
        d[w].incrOccurrences()

print("Word 'the' occurred " + str(d["the"].getOccurrences()) + " times")
print("There are " + str(len(d.keys())) + " words in the text")

