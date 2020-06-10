#!/usr/bin/env python

import turtle
import math
from nltk.corpus import wordnet as wn
import warnings
import string
from ghost import ghost
from maxsim import maxsim

def pronouns(word, x, y, box, t):

    print("POS: Pronouns, Your word: " + word + ", Suggested Word: " + word)

    boxf = float(box)
    col = "#000000"
    t.fillcolor(col)
    #bottom
    if word == "he" or word == "she" or word == "him" or word == "his" or word == "hers" or word == "her":
        y = y - 2*boxf/3
        t.begin_fill()
        ghost(t, x, y+boxf/1.1)
        t.circle(boxf/50, 360)
        t.end_fill()
        if word == "her" or word =="hers" or word=="his":
            ghost(t, x-boxf/10, y+boxf/1.1)
            t.setheading(270)
            t.circle(boxf/10, 180)
        return 1
    if word == "they" or word == "their" or word == "theirs":
        y = y - 2*boxf/3
        t.begin_fill()
        ghost(t, x, y+boxf/1.1)
        t.circle(boxf/50, 360)
        t.end_fill()
        t.begin_fill()
        ghost(t, x+boxf/10, y+boxf/1.1)
        t.circle(boxf/50, 360)
        t.end_fill()
        if word == "their" or word == "theirs":
            ghost(t, x-boxf/15, y+boxf/1.1)
            t.setheading(270)
            t.circle(boxf/8, 180)
        return 1
    if word == "somebody":
        y = y - 2*boxf/3
        t.begin_fill()
        ghost(t, x, y+boxf/1.3)
        t.circle(boxf/50, 360)
        t.end_fill()
        t.begin_fill()
        ghost(t, x+boxf/10, y+boxf/1.3-boxf/10)
        t.circle(boxf/50, 360)
        t.end_fill()
        return 1
    if word == "all":
        y = y - 2*boxf/3
        t.begin_fill()
        ghost(t, x, y+boxf/1.3)
        t.circle(boxf/50, 360)
        t.end_fill()
        t.begin_fill()
        ghost(t, x, y+boxf/1.3-boxf/10)
        t.circle(boxf/50, 360)
        t.end_fill()
        return 1
    #middle
    if word == "you" or word == "yours" or word == "your":
        y = y - boxf/3
        t.begin_fill()
        ghost(t, x, y+boxf/1.1)
        t.circle(boxf/50, 360)
        t.end_fill()
        if word == "your" or word =="yours":
            ghost(t, x-boxf/10, y+boxf/1.1)
            t.setheading(270)
            t.circle(boxf/10, 180)
        return 1
    if word == "another":
        y = y - boxf/3
        t.begin_fill()
        ghost(t, x, y+boxf/1.3)
        t.circle(boxf/50, 360)
        t.end_fill()
        t.begin_fill()
        ghost(t, x+boxf/10, y+boxf/1.3-boxf/10)
        t.circle(boxf/50, 360)
        t.end_fill()
        return 1
    if word == "every":
        y = y - boxf/3
        t.begin_fill()
        ghost(t, x, y+boxf/1.3)
        t.circle(boxf/50, 360)
        t.end_fill()
        t.begin_fill()
        ghost(t, x, y+boxf/1.3-boxf/10)
        t.circle(boxf/50, 360)
        t.end_fill()
        return 1
    if word == "which":
        y = y - boxf/3
        t.begin_fill()
        ghost(t, x, y+boxf/1.3)
        t.circle(boxf/50, 360)
        t.end_fill()
        t.begin_fill()
        ghost(t, x+boxf/10, y+boxf/1.3-boxf/10)
        t.circle(boxf/50, 360)
        t.end_fill()
        t.begin_fill()
        ghost(t, x+2*boxf/10, y+boxf/1.3)
        t.circle(boxf/50, 360)
        t.end_fill()
        return 1
    if word == "thou" or word == "thy" or word == "thine":
        y = y - boxf/3
        t.begin_fill()
        ghost(t, x, y+boxf/1.1)
        t.circle(boxf/50, 360)
        t.end_fill()
        if word == "thine" or word =="thy":
            ghost(t, x-boxf/10, y+boxf/1.1)
            t.setheading(270)
            t.circle(boxf/10, 180)
        return 1
    #top
    if word == "i" or word == "mine" or word == "my":
        t.begin_fill()
        ghost(t, x, y+boxf/1.1)
        t.circle(boxf/50, 360)
        t.end_fill()
        if word == "mine" or word =="my":
            ghost(t, x-boxf/10, y+boxf/1.1)
            t.setheading(270)
            t.circle(boxf/10, 180)
        return 1
    if word == "we" or word == "us" or word == "our" or word == "ours":
        t.begin_fill()
        ghost(t, x, y+boxf/1.1)
        t.circle(boxf/50, 360)
        t.end_fill()
        t.begin_fill()
        ghost(t, x+boxf/10, y+boxf/1.1)
        t.circle(boxf/50, 360)
        t.end_fill()
        if word == "our" or word == "ours":
            ghost(t, x-boxf/15, y+boxf/1.1)
            t.setheading(270)
            t.circle(boxf/8, 180)
        return 1
    if word == "this":
        t.begin_fill()
        ghost(t, x, y+boxf/1.3)
        t.circle(boxf/50, 360)
        t.end_fill()
        t.begin_fill()
        ghost(t, x+boxf/10, y+boxf/1.3+boxf/10)
        t.circle(boxf/50, 360)
        t.end_fill()
        return 1
    if word == "that":
        t.begin_fill()
        ghost(t, x, y+boxf/1.3)
        t.circle(boxf/50, 360)
        t.end_fill()
        t.begin_fill()
        ghost(t, x+boxf/10, y+boxf/1.3-boxf/10)
        t.circle(boxf/50, 360)
        t.end_fill()
        return 1
    if word == "any":
        t.begin_fill()
        ghost(t, x, y+boxf/1.3)
        t.circle(boxf/50, 360)
        t.end_fill()
        t.begin_fill()
        ghost(t, x, y+boxf/1.3-boxf/10)
        t.circle(boxf/50, 360)
        t.end_fill()
        return 1
    if word == "who":
        t.begin_fill()
        ghost(t, x, y+boxf/1.3)
        t.circle(boxf/50, 360)
        t.end_fill()
        t.begin_fill()
        ghost(t, x+boxf/10, y+boxf/1.3-boxf/10)
        t.circle(boxf/50, 360)
        t.end_fill()
        t.begin_fill()
        ghost(t, x+2*boxf/10, y+boxf/1.3)
        t.circle(boxf/50, 360)
        t.end_fill()
        return 1  