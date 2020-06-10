#!/usr/bin/env python

import turtle
import math
from nltk.corpus import wordnet as wn
import warnings
import string
from ghost import ghost
from maxsim import maxsim

def prepositions(word, x, y, box, t): 

    print("POS: Prepositions, Your word: " + word + ", Suggested Word: " + word)

    boxf = float(box)
    #x = x+boxf/20
    #bottom
    #actually "out of"
    if word == "out":
        ghost(t, x, y)
        t.setheading(270)
        t.circle(box/10, 180)
        return 1
    if word == "concerning":
        ghost(t, x, y)
        t.setheading(90)
        t.circle(box/10, 180)
        return 1
    if word == "over":
        ghost(t, x, y)
        t.setheading(270)
        t.circle(box/10, 180)
        ghost(t, x+16, y)
        t.setheading(270)
        t.circle(box/10, 180)
        return 1
    if word == "at":
        ghost(t, x, y)
        t.setheading(90)
        t.circle(box/10, 180)
        ghost(t, x+16, y)
        t.setheading(90)
        t.circle(box/10, 180)
        return 1
    if word == "against":
        ghost(t, x, y)
        t.setheading(180)
        t.circle(box/10, 180)
        return 1
    if word == "for":
        ghost(t, x, y)
        t.setheading(0)
        t.circle(box/10, 180)
        return 1
    if word == "through":
        ghost(t, x, y)
        t.setheading(0)
        t.circle(box/10, 180)
        ghost(t, x, y-16)
        t.setheading(0)
        t.circle(box/10, 180)
        return 1
    if word == "beside":
        ghost(t, x, y)
        t.setheading(180)
        t.circle(box/10, 180)
        ghost(t, x, y-16)
        t.setheading(180)
        t.circle(box/10, 180)
        return 1
    if word == "before":
        ghost(t, x, y)
        t.setheading(270)
        t.circle(box/10, 180)
        ghost(t, x+32, y)
        t.setheading(90)
        t.circle(box/10, 180)
        return 1
    if word == "behind":
        ghost(t, x, y+8)
        t.setheading(90)
        t.circle(box/10, 180)
        ghost(t, x, y+8)
        t.setheading(270)
        t.circle(box/10, 180)
        return 1
    if word == "between" or x == "betwixt":
        ghost(t, x, y)
        t.setheading(0)
        t.circle(box/10, 180)
        ghost(t, x, y)
        t.setheading(180)
        t.circle(box/10, 180)
        return 1
    #middle
    if word == "by":
        ghost(t, x, y+20)
        t.setheading(270)
        t.circle(box/10, 180)
        return 1
    if word == "for":
        ghost(t, x, y+20)
        t.setheading(90)
        t.circle(box/10, 180)
        return 1
    if word == "from":
        ghost(t, x, y+20)
        t.setheading(270)
        t.circle(box/10, 180)
        ghost(t, x+16, y+20)
        t.setheading(270)
        t.circle(box/10, 180)
        return 1
    if word == "off":
        ghost(t, x, y+20)
        t.setheading(90)
        t.circle(box/10, 180)
        ghost(t, x+16, y+20)
        t.setheading(90)
        t.circle(box/10, 180)
        return 1
    if word == "without":
        ghost(t, x, y+20)
        t.setheading(180)
        t.circle(box/10, 180)
        return 1
    if word == "with":
        ghost(t, x, y+20)
        t.setheading(0)
        t.circle(box/10, 180)
        return 1
    if word == "downwards":
        ghost(t, x, y+23)
        t.setheading(270)
        t.circle(box/10, 180)
        ghost(t, x+32, y+23)
        t.setheading(90)
        t.circle(box/10, 180)
        return 1
    if word == "below":
        ghost(t, x, y+31)
        t.setheading(90)
        t.circle(box/10, 180)
        ghost(t, x, y+31)
        t.setheading(270)
        t.circle(box/10, 180)
        return 1
    if word == "beyond":
        ghost(t, x, y+17)
        t.setheading(180)
        t.circle(box/10, 180)
        ghost(t, x, y+17)
        t.setheading(0)
        t.circle(box/10, 180)
        return 1
    
    #top
    if word == "of":
        ghost(t, x, y+box/1.1)
        t.setheading(270)
        t.circle(box/10, 180)
        return 1
    if word == "to":
        ghost(t, x, y+box/1.1)
        t.setheading(270)
        t.circle(box/10, 180)
        ghost(t, x+box/4.66, y+box/1.1)
        t.setheading(270)
        t.circle(box/10, 180)
        return 1
    if word == "about":
        ghost(t, x, y+box/1.33)
        t.setheading(90)
        t.circle(box/10, 180)
        ghost(t, x+box/4.66, y+box/1.33)
        t.setheading(90)
        t.circle(box/10, 180)
        return 1
    if word == "instead":
        ghost(t, x, y+box/1.1)
        t.setheading(180)
        t.circle(box/10, 180)
        return 1
    if word == "into":
        ghost(t, x, y+box/1.33)
        t.setheading(0)
        t.circle(box/10, 180)
        ghost(t, x, y+box/1.8)
        t.setheading(0)
        t.circle(box/10, 180)
        return 1
    if word == "in":
        ghost(t, x, y+box/1.1)
        t.setheading(180)
        t.circle(box/10, 180)
        ghost(t, x, y+box/1.43)
        t.setheading(180)
        t.circle(box/10, 180)
        return 1
    if word == "upwards":
        ghost(t, x+box/2.5, y+box/1.33)
        t.setheading(90)
        t.circle(box/10, 180)
        ghost(t, x, y+box/1.33)
        t.setheading(270)
        t.circle(box/10, 180)
        return 1
    if word == "above":
        ghost(t, x, y+box/1.33)
        t.setheading(90)
        t.circle(box/10, 180)
        ghost(t, x, y+box/1.33)
        t.setheading(270)
        t.circle(box/10, 180)
        return 1
    if word == "according":
        ghost(t, x, y+box/1.33)
        t.setheading(0)
        t.circle(box/10, 180)
        return 1
    if word == "upon":
        ghost(t, x, y+box/1.33)
        t.setheading(0)
        t.circle(box/10, 180)
        ghost(t, x, y+box/1.33)
        t.setheading(180)
        t.circle(box/10, 180)
        return 1
    if word == "under":
        ghost(t, x, y+box/1.1)
        t.setheading(180)
        t.circle(box/10, 180)
        ghost(t, x, y+box/1.95)
        t.setheading(0)
        t.circle(box/10, 180)
        return 1
    
    return 0