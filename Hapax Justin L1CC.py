# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:35:59 2021

@author: WINDOWS10
"""
import re
path=r"D:\test\Text.txt"
def hapax_function(give_your_path):
    file = open(give_your_path)
    list_of_words = re.findall('\w+', file.read().lower())
    freqs = {key: 0 for key in list_of_words}
    for word in list_of_words:
        freqs[word] += 1
    for word in freqs:
        if freqs[word] == 1:
            print(word)

hapax_function(path)

