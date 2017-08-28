# put your code here.
my_file = open("test.txt")


def word_count(my_file):

    poem = {}
    for line in my_file:
        line = line.lower().rstrip()
   #     for punctuation in line:
   #         if punctuation is "?" or "," or "."
    #        delete punctuation[i]
        spl = line.split(" ")
        for words in spl:
            poem[words] = poem.get(words, 0) + 1
    for k, v in poem.iteritems():
        print k, v


word_count(my_file)
