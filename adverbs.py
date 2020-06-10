#!/usr/bin/env python

import turtle
import math
from nltk.corpus import wordnet as wn
import warnings
import string
from ghost import ghost
from maxsim import maxsim

def adverbs(word, x, y, box, t):
	#if syn1 is length of zero, just do it for any part of speech

    print("POS: Adverbs, Your word: " + word + ", Suggested Word: " + word)

    boxf = float(box)                                                   
   #bottom 
    if word == "as":
        y = y - 2*boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(0)
        t.fd(boxf*.1)
        t.setheading(90)
        t.fd(boxf*.1)
        return 1
    if word == "so":
        y = y - 2*boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(180)
        t.fd(boxf*.1)
        t.setheading(90)
        t.fd(boxf*.1)
        return 1
    if word == "less":
        y = y - 2*boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(0)
        t.fd(boxf*.1)
        t.setheading(270)
        t.fd(boxf*.1)
        return 1
    if word == "least":
        y = y - 2*boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(180)
        t.fd(boxf*.1)
        t.setheading(270)
        t.fd(boxf*.1)
        return 1
    if word == "while":
        y = y - 2*boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(0)
        t.fd(2*boxf*.1)
        t.setheading(180)
        t.fd(boxf*.1)
        t.setheading(90)
        t.fd(boxf*.1)
        return 1
    #mid
    if word == "maybe":
        y = y - boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(0)
        t.fd(boxf*.1)
        t.setheading(90)
        t.fd(boxf*.1)
        return 1
    if word == "truly":
        y = y - boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(180)
        t.fd(boxf*.1)
        t.setheading(90)
        t.fd(boxf*.1)
        return 1
    if word == "more":
        y = y - boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(0)
        t.fd(boxf*.1)
        t.setheading(270)
        t.fd(boxf*.1)
        return 1
    if word == "most":
        y = y - boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(180)
        t.fd(boxf*.1)
        t.setheading(270)
        t.fd(boxf*.1)
        return 1
    if word == "yet":
        y = y - boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(0)
        t.fd(2*boxf*.1)
        t.setheading(180)
        t.fd(boxf*.1)
        t.setheading(90)
        t.fd(boxf*.1)
        return 1
    if word == "until":
        y = y - boxf/3
        ghost(t, x, y+box/1.1)
        t.setheading(0)
        t.fd(2*boxf*.1)
        t.setheading(180)
        t.fd(boxf*.1)
        t.setheading(270)
        t.fd(boxf*.1)
        return 1
    if word == "again":
        y = y - boxf/3
        ghost(t, x, y+box/1.3)
        t.setheading(90)
        t.fd(2*boxf*.1)
        t.setheading(270)
        t.fd(boxf*.1)
        t.setheading(180)
        t.fd(boxf*.1)
        return 1
    if word == "scarce":
        y = y - boxf/3
        ghost(t, x, y+box/1.3)
        t.setheading(90)
        t.fd(2*boxf*.1)
        t.setheading(270)
        t.fd(boxf*.1)
        t.setheading(0)
        t.fd(boxf*.1)
        t.setheading(180)
        t.fd(2*boxf*.1)
        return 1
    #top
    if word == "yes":
        ghost(t, x, y+box/1.1)
        t.setheading(0)
        t.fd(boxf*.1)
        t.setheading(90)
        t.fd(boxf*.1)
        return 1
    if word == "no":
        ghost(t, x, y+box/1.1)
        t.setheading(180)
        t.fd(boxf*.1)
        t.setheading(90)
        t.fd(boxf*.1)
        return 1
    if word == "how":
        ghost(t, x, y+box/1.1)
        t.setheading(0)
        t.fd(boxf*.1)
        t.setheading(270)
        t.fd(boxf*.1)
        return 1
    if word == "rather":
        ghost(t, x, y+box/1.1)
        t.setheading(0)
        t.fd(2*boxf*.1)
        t.setheading(180)
        t.fd(boxf*.1)
        t.setheading(90)
        t.fd(boxf*.1)
        return 1
    if word == "than":
        ghost(t, x, y+box/1.1)
        t.setheading(0)
        t.fd(2*boxf*.1)
        t.setheading(180)
        t.fd(boxf*.1)
        t.setheading(270)
        t.fd(boxf*.1)
        return 1
    if word == "together":
        ghost(t, x, y+box/1.3)
        t.setheading(90)
        t.fd(2*boxf*.1)
        t.setheading(270)
        t.fd(boxf*.1)
        t.setheading(180)
        t.fd(boxf*.1)
        return 1
    if word == "only":
        ghost(t, x, y+box/1.3)
        t.setheading(90)
        t.fd(2*boxf*.1)
        t.setheading(270)
        t.fd(boxf*.1)
        t.setheading(0)
        t.fd(boxf*.1)
        return 1
    if word == "almost":
        ghost(t, x, y+box/1.3)
        t.setheading(90)
        t.fd(2*boxf*.1)
        t.setheading(270)
        t.fd(boxf*.1)
        t.setheading(0)
        t.fd(boxf*.1)
        t.setheading(180)
        t.fd(2*boxf*.1)
        return 1