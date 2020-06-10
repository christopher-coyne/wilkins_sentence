#!/usr/bin/env python

import turtle
import math
from nltk.corpus import wordnet as wn
import warnings
import string
from ghost import ghost
from maxsim import maxsim

def conjunctions(word, x, y, box, t):
	#if syn1 is length of zero, just do it for any part of speech

    print("POS: Conjunctions, Your word: " + word + ", Suggested Word: " + word)

    boxf = float(box)
    #bottom
    if word == "if":
        y = y - 2*boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(315)
        t.fd(boxf*.1)
        t.setheading(45)
        t.fd(boxf*.1)
        return 1
    if word == "unless":
        y = y - 2*boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(45)
        t.fd(boxf*.1)
        t.setheading(315)
        t.fd(boxf*.1)
        return 1
    if word == "or":
        y = y - 2*boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(315)
        t.fd(boxf*.1)
        t.setheading(225)
        t.fd(boxf*.1)
        return 1
    if word == "either":
        y = y - 2*boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(225)
        t.fd(boxf*.1)
        t.setheading(315)
        t.fd(boxf*.1)
        return 1 
    if word == "wherefore":
        y = y - 2*boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(315)
        t.fd(boxf*.1)
        t.setheading(45)
        t.fd(boxf*.1)
        t.setheading(225)
        t.fd(boxf*.2)
        return 1
    if word == "therefore":
        y = y - 2*boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(315)
        t.fd(boxf*.1)
        t.setheading(45)
        t.fd(boxf*.1)
        t.setheading(225)
        t.fd(boxf*.1)
        t.setheading(315)
        t.fd(boxf*.1)
        return 1
    #middle 
    if word == "and":
        y = y - boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(315)
        t.fd(boxf*.1)
        t.setheading(45)
        t.fd(boxf*.1)
        return 1
    if word == "neither":
        y = y - boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(45)
        t.fd(boxf*.1)
        t.setheading(315)
        t.fd(boxf*.1)
        return 1 
    if word == "although":
        y = y - boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(315)
        t.fd(boxf*.1)
        t.setheading(225)
        t.fd(boxf*.1)
        return 1
    if word == "for":
        y = y - boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(315)
        t.fd(boxf*.1)
        t.setheading(45)
        t.fd(boxf*.1)
        t.setheading(225)
        t.fd(boxf*.2)
        return 1
    if word == "because":
        y = y - boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(315)
        t.fd(boxf*.1)
        t.setheading(45)
        t.fd(boxf*.1)
        t.setheading(225)
        t.fd(boxf*.1)
        t.setheading(315)
        t.fd(boxf*.1)
        return 1
    if word == "also":
        y = y - boxf/3
        ghost(t, x, y+box/1.3)
        t.setheading(45)
        t.fd(boxf*.1)
        t.setheading(315)
        t.fd(boxf*.1)
        t.setheading(135)
        t.fd(boxf*.2)
        return 1
    #top
    if word == "whether":
        ghost(t, x, y+box/1.1)
        t.setheading(315)
        t.fd(boxf*.1)
        t.setheading(45)
        t.fd(boxf*.1)
        return 1
    if word == "indeed":
        ghost(t, x, y+box/1.1)
        t.setheading(315)
        t.fd(boxf*.1)
        t.setheading(225)
        t.fd(boxf*.1)
        return 1
    if word == "but":
        ghost(t, x, y+box/1.1)
        t.setheading(225)
        t.fd(boxf*.1)
        t.setheading(315)
        t.fd(boxf*.1)
        return 1 
    if word == "that":
        ghost(t, x, y+box/1.1)
        t.setheading(315)
        t.fd(boxf*.1)
        t.setheading(45)
        t.fd(boxf*.1)
        t.setheading(225)
        t.fd(boxf*.2)
        return 1
    if word == "whereas":
        ghost(t, x, y+box/1.3)
        t.setheading(45)
        t.fd(boxf*.1)
        t.setheading(315)
        t.fd(boxf*.1)
        t.setheading(135)
        t.fd(boxf*.2)
        return 1 