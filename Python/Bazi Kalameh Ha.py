"""
--------------------------------------------------
Name    : Bazi Kalameh Ha
Author  : Danial Khorasanizadeh
Link    : quera.ir/problemset/technology/87181
Date    : 10/Feb/2021
--------------------------------------------------
"""


def words_check(text):
    text = r""+text
    text = text.split()
    newText = list()
    for word in text:
        word = word.lower()
        notEnglish = 0
        tempWord = list()
        for letter in word:
            if 97 <= ord(letter) <= 122:
                tempWord.append(letter)
            else:
                notEnglish += 1
        tempWord = "".join(map(str, tempWord)).title()
        if notEnglish < len(word)/2:
            newText.append(tempWord)
    words = dict()
    for word in newText:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words
