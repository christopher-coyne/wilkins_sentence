#!/usr/bin/env python

import turtle
import math
from nltk.corpus import wordnet as wn
import warnings
import string
from ghost import ghost

def maxsim(word, wordlist, postag):


    sameword = None
    for w2 in wordlist:
        if word == w2:
            sameword = word
    if sameword == None:
        return [wordlist[0], 0]
    return [sameword, 1]

