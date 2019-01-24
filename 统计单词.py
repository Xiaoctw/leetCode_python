import sys
import string
print(string.whitespace+string.punctuation)
#无用的东西组成一个字符串，用来消去他们
strip=string.whitespace+string.punctuation+string.digits+"\""
words={}
file=open("统计单词","r")
for line in file.readlines():
    for word in line.lower().split():
        word=word.strip(strip)
        if len(word)>2:
            words[word]=words.get(word,0)+1
for word in sorted(words):
    print("{0} occurs {1} times".format(word,words[word]))