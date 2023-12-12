#-------------------------------------------------------------------
# Written by Carter Stickler, December 2023.
#
# Anyone may freely copy or modify this program. 
#   Assuming you can find it in my hidden github. 
#   Or if you're the instructor, and I wound up handing this to you.
#-------------------------------------------------------------------
import string
import sys #I hope importing this here was okay. I didn't want you to have to make manual edits to the path of the files in order to run this.

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

def countWordOccurances(words, x):
    count = 0
    for word in words:
        if (word == x):
            count = count + 1
    return count

def countWords(words): #I'm not sure why it's returning those random ": 847" lines in the file it generates. I get the extra spaces considering the punctuation isn't removing next lines and other items, bit I find it very weird that those lines are appearing so often. However, even with those lines, this technically passes the requirements of the task I believe. If I had more time to work on it, I would refine it and keep going, but I've been going on this for an hour plus, and I don't have the answer to that one. I'm okay loosing some points for this assignment, haha. Sorry for the late submission by the way.
    finalCount = """Word              Count \n======================="""
    completed = []
    for word in words:
        if word not in completed:
            occurances = countWordOccurances(words, word)
            finalCount += "\n"+str(word)+": "+str(occurances)
            completed += word
    
    return finalCount

aliceBook = open(sys.path[0] + "/pg19033.txt", "r", encoding="utf8")
aliceWords = open(sys.path[0] + "./alice_words.txt", "w+", encoding="utf8")
readBook = aliceBook.read()

removedPunctuation = remove_punctuation(readBook)
wordList = removedPunctuation.split(" ")

aliceWords.write(countWords(wordList))
