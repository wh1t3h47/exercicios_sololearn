#!/bin/env python3

file = open("/usercode/files/books.txt", "r")
words = file.read().split()
abrev = ""
for word in words:
    if (len(word)):
        abrev = abrev + word[0]
print(abrev)


file.close()
