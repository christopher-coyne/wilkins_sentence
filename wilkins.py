#!/usr/bin/env python

import turtle
import re
import math
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import nltk
nltk.download("averaged_perceptron_tagger")
import numpy as np
import warnings
import string
import os
from pronouns import pronouns
from conjunctions import conjunctions
from adverbs import adverbs
from prepositions import prepositions
from maxsim import maxsim
from nltk.stem import WordNetLemmatizer
from nounify import *


#prints if word is unknown, meaning it is not in wordnet or Wilkins's corpus
def unk_print(x, y, boxf):
    col = "#228B22"
    ghost(x+boxf/2, y+boxf/2)
    t.fillcolor(col)
    t.begin_fill()
    t.circle(boxf/10, 360)
    t.end_fill()
    return 1

wn_lemmas = set(wn.all_lemma_names())

Letternum = 0
BORDER = 0
BOX_WIDTH, BOX_HEIGHT = 1000, 700  # letter bounding box
WIDTH, HEIGHT = BOX_WIDTH, BOX_HEIGHT  # letter size

g = input("Enter your sentence, no capitalizations:")
wordlist = re.sub("[^\w]", " ",  g).split()
print("your input: ")
print(wordlist)

pos_tags = nltk.pos_tag(wordlist)
print(pos_tags)


s = turtle.getscreen()
s.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
#s.setworldcoordinates(0, 0, WIDTH, HEIGHT)
t = turtle.Turtle()
t.ht()
turtle.ht()

pronounlist = ["he", "she", "him", "his", "hers", "her", "they",
    "their", "theirs", "somebody", "you", "your", "yours", "another",
    "every", "which", "i", "my", "mine", "we", "us", "our", "ours",
    "this", "that", "any", "who"]

prepositionlist = ["out", "concerning", "over", "at", "against", "for", "through",
    "beside", "before", "behind", "between", "betwixt", "by", "from",
    "off", "without", "with", "downwards", "below", "beyond", "of", "to", "about",
    "instead", "into", "in", "upwards", "above", "according", "upon", "under"]

conjunctionlist = ["if", "unless", "or", "either", "wherefore", "therefore", "and",
    "neither", "although", "for", "because", "also", "whether", "indeed",
    "but", "that", "whereas"]

adverblist = ["as", "so", "less", "least", "while", "maybe", "truly",
    "more", "most", "yet", "until", "again", "scarce", "yes", "no"
    "how", "rather", "than", "together", "only", "almost"]

def ghost(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def noun(myword, x, y, pos):
    boxf = float(box)
    similarities = []
    line = .6*boxf

    
    if pos == "NN" or pos == "NNP" or pos == "NNS" or pos == "UH":
        new_pos = "n"
        if len(wn.synsets(myword, pos="n")) == 0:
            if len(wn.synsets(myword)) == 0:
                unk_print(x, y, boxf)
                print("your word: " + myword + ", UNKNOWN")
                return
            else:
                syn1 = wn.synsets(myword)[0]
        else:
            syn1 = wn.synsets(myword, pos="n")[0]

    elif pos == "VB" or pos == "VBD" or pos == "VBG" or pos == "VBN" or pos == "VBP" or pos == "VBZ" or pos == "MD":
        #to be is a special verb, listed separately from corpus
        if myword == "be":
            y = y+boxf/2
            ghost(x, y)
            t.circle(boxf/30, 360)
            return
        new_pos = "v"
        print(myword)
        print("ADJECTIVE TO NOUN:")
        if len(nounify2(myword, "v", "n"[0])) == 0:
            print("your word: " + myword + ", UNKNOWN")
            unk_print(x, y, boxf)
            return
        print(nounify2(myword, "v", "n")[0][0])
        syn1 = wn.synsets(nounify2(myword, "v", "n")[0][0], pos="n")[0]


    elif pos == "RB" or pos == "RBR" or pos == "RBS" or pos == "WRB" or pos == "PDT" or pos == "MD" or pos == "EX":
        new_pos = "r"
        #syn1 = wn.synsets(myword, pos="r")[0]
        print("adverb TO adj:")
        print(nounify3(myword))
        if len(nounify3(myword)) == 0:
            print("your word: " + myword + ", UNKNOWN")
            unk_print(x, y, boxf)
            return
        new_adj = nounify3(myword)[0]
        print(nounify2(new_adj, "a", "n")[0][0])
        syn1 = wn.synsets(nounify2(new_adj, "a", "n")[0][0], pos="n")[0]
        print(syn1)

    elif pos == "JJ" or pos == "JJR" or pos == "JJS" or pos == "J":
        new_pos = "a"
        print(wn.synsets(myword))
        #syn1 = wn.synsets(myword, pos="a")[0]
        print("ADJECTIVE TO NOUN:")
        if len(nounify2(myword, "a", "n"[0])) == 0:
            print("your word: " + myword + ", UNKNOWN")
            unk_print(x, y, boxf)
            return
        print(nounify2(myword, "a", "n")[0][0])
        syn1 = wn.synsets(nounify2(myword, "a", "n")[0][0], pos="n")[0]
    
    
    ghost(x+(float(box)/5), y+(float(box)/2))
    t.fd(math.floor(box)*.6)

    f = open("wilk.txt", "r")

    mostsim = [0, "cat", "difnum", "word", 1, "1"]
    category = 0
    dif = 0
    speccount = 1
    exclude = set(string.punctuation)

    mylines = f.readlines()
    for line in mylines:
        split = line.split("(")
        for dif in split:
            dif = ''.join(ch for ch in dif if ch not in exclude)
            species = dif.split()
            if len(species) > 0:
                if "xxx" in species[0]:
                    category = species[0][3:]
                elif species[0][-1].isdigit():
                    difnum = species[0][-1]
                    speccount = 1
                else:
                    for word in species:
                        if word in wn_lemmas:
                            syn2 = wn.synsets(word)[0]
                            sim = wn.wup_similarity(syn1,syn2)
                            if sim == None:
                                sim = 0
                            if sim > mostsim[0]:
                                mostsim[0] = sim
                                mostsim[1] = category
                                mostsim[2] = difnum
                                mostsim[3] = word
                                mostsim[4] = speccount
                                mostsim[5] = species.index(word)
                    speccount += 1
                    

    print("POS: " + pos + ", your word: " + myword + ", suggested word: " + mostsim[3] + ", category: " + 
          mostsim[1] + ", difference number: " + mostsim[2] + ", species number: " + str(mostsim[4]))
    
    #draw base shape here:
    if "stone" in mostsim[1]:
        ghost(x+(float(box)/2), y+(float(box)/2))
        t.setheading(270)
        t.fd(math.floor(box)*.2)
    
    if "metal" in mostsim[1]:
        ghost(x+float(box)*.4, y+float(box)*.6)
        t.setheading(315)
        t.fd(float(box)*.3)
    
    if "exanimals" in mostsim[1]:
        ghost(x+(float(box)/2), y+(float(box)/2))
        t.setheading(90)
        t.fd(float(box)*.2)
        t.setheading(225)
        t.fd(boxf*.1)
        
    if "corpactions" in mostsim[1]:
        ghost(x+(float(box)/2), y+(float(box)/2))
        t.setheading(180)
        t.circle(boxf/10, 180)
    
    if "spiritactions" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(0)
        t.circle(boxf/10, 190)
    
    if "manners" in mostsim[1]:
        ghost(x+boxf/2+boxf/10, y+boxf/2)
        t.setheading(90)
        t.circle(boxf/10, 190)
        
    if "motion" in mostsim[1]:
        ghost(x+boxf/2, y+2*(boxf/10)+boxf/2)
        t.setheading(180)
        t.circle(boxf/10, 190)
    
    if "operation" in mostsim[1]:
        ghost(x+boxf/2, y-2*(boxf/10)+boxf/2)
        t.setheading(0)
        t.circle(boxf/10, 190)
        
    if "ecrel" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(0)
        t.circle(boxf/10, 200)
        ghost(x+boxf/2, y-2*(boxf/10)+boxf/2)
        t.setheading(0)
        t.circle(boxf/10, 200)
        
    if "ecpos" in mostsim[1]:
        ghost(x+(float(box)/2), y+(float(box)/2))
        t.setheading(180)
        t.circle(boxf/10, 180)
        ghost(x+boxf/2, y+2*(boxf/10)+boxf/2)
        t.setheading(180)
        t.circle(boxf/10, 190)
        
    if "provisions" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(0)
        t.circle(boxf/10, 190)
        ghost(x+(float(box)/2), y+(float(box)/2))
        t.setheading(180)
        t.circle(boxf/10, 180)
        
    if "civrel" in mostsim[1]:
        ghost(x+boxf/2, y+2*(boxf/10)+boxf/2)
        t.setheading(180)
        t.circle(boxf/10, 190)
        ghost(x+boxf/2, y-2*(boxf/10)+boxf/2)
        t.setheading(0)
        t.circle(boxf/10, 190)
    
    if "judrel" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.circle(boxf/10, 360)
        
    if "milrel" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2-(boxf/5))
        t.circle(boxf/10, 360)
        
    if "navrel" in mostsim[1]:
        ghost(x+boxf/2-boxf/20, y+boxf/2)
        t.setheading(45)
        t.fd(boxf/15)
        ghost(x+boxf/2+boxf/20, y+boxf/2)
        t.setheading(135)
        t.fd(boxf/15)
        ghost(x+boxf/2+boxf/15, y+boxf/2+boxf/4.5)
        t.circle(boxf/10, 360)
        
    if "eclrel" in mostsim[1]:
        ghost(x+boxf/2-boxf/20, y+boxf/2)
        t.setheading(315)
        t.fd(boxf/15)
        ghost(x+boxf/2+boxf/20, y+boxf/2)
        t.setheading(225)
        t.fd(boxf/15)
        ghost(x+boxf/2-boxf/15, y+boxf/2-boxf/11)
        t.circle(boxf/10, 360)
        
    if "sensqual" in mostsim[1]:
        ghost(x+boxf/2-(boxf/10), y+boxf/2)
        t.setheading(270)
        t.circle(boxf/10, 190)
    
    if "space" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(270)
        t.fd(float(box)*.2)
        t.circle(boxf/20, 190)
        
    if "measure" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(90)
        t.fd(float(box)*.2)
        t.circle(boxf/20, 190)
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(270)
        t.fd(float(box)*.2)
        
    if "magnitude" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(90)
        t.fd(float(box)*.2)
        t.circle(boxf/20, 190)
        
    if "naturalp" in mostsim[1]:
        ghost(x+boxf/2-10, y+boxf/2+10)
        t.setheading(270)
        t.circle(boxf/10, 190)
    
    if "disease" in mostsim[1]:
        ghost(x+boxf/2-(boxf/10), y+boxf/2)
        t.setheading(270)
        t.circle(boxf/10, 190)
        ghost(x+boxf/2+boxf/10, y+boxf/2)
        t.setheading(90)
        t.circle(boxf/10, 190)
        
    if "gparts" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(90)
        t.fd(boxf*.2)
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(270)
        t.fd(boxf*.2)
        t.setheading(45)
        t.fd(boxf*.1)
    
    if "pparts" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(90)
        t.fd(boxf*.2)
        t.setheading(225)
        t.fd(boxf*.1)
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(270)
        t.fd(boxf*.2)
    
    if "beast" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(270)
        t.fd(boxf*.2)
        t.setheading(45)
        t.fd(boxf*.1)
        
    if "bird" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(90)
        t.fd(boxf*.2)
        t.setheading(180)
        t.fd(boxf*.1)
        
    if "fish" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(270)
        t.fd(boxf*.2)
        t.setheading(45)
        t.fd(boxf*.1)
    
    if "tree" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(45)
        t.fd(boxf*.2)
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(225)
        t.fd(boxf*.2)
    
    if "shrub" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(225)
        t.fd(boxf*.2)
    
    if "herbseed" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(45)
        t.fd(boxf*.2)
    
    if "herbflower" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(315)
        t.fd(boxf*.2)
    
    if "herbleaf" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(135)
        t.fd(boxf*.2)
    
    if "element" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(90)
        t.fd(boxf*.2)
    
    if "godworld" in mostsim[1]:
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(90)
        t.fd(boxf*.2)
        ghost(x+boxf/2, y+boxf/2)
        t.setheading(270)
        t.fd(boxf*.2)
    
    if "discourse" in mostsim[1]:
        t.pencolor("white")
        ghost(x+boxf/2-(boxf/10), y+boxf/2)
        t.setheading(0)
        t.fd(boxf/5)
        t.pencolor("black")
        ghost(x+boxf/2-(boxf/10), y+boxf/2)
        t.setheading(270)
        t.circle(boxf/10, 180)
    
    if "tranrelact" in mostsim[1]:
        t.pencolor("white")
        ghost(x+boxf/2-(boxf/10), y+boxf/2)
        t.setheading(0)
        t.fd(boxf/5)
        t.pencolor("black")
        ghost(x+boxf/2+boxf/10, y+boxf/2)
        t.setheading(90)
        t.circle(boxf/10, 180)
        
    if "tranmix" in mostsim[1]:
        t.pencolor("white")
        ghost(x+boxf/2-(boxf/20), y+boxf/2)
        t.setheading(0)
        t.fd(boxf/10)
        t.pencolor("black")
        ghost(x+boxf/2-boxf/20, y+boxf/2)
        t.setheading(315)
        t.fd(boxf/15)
        ghost(x+boxf/2+boxf/20, y+boxf/2)
        t.setheading(225)
        t.fd(boxf/15)
        ghost(x+boxf/2-boxf/15, y+boxf/2-boxf/11)
        
    if "trangen" in mostsim[1]:
        t.pencolor("white")
        ghost(x+boxf/2-(boxf/20), y+boxf/2)
        t.setheading(0)
        t.fd(boxf/10)
        t.pencolor("black")
        ghost(x+boxf/2-boxf/20, y+boxf/2)
        t.setheading(45)
        t.fd(boxf/15)
        ghost(x+boxf/2+boxf/20, y+boxf/2)
        t.setheading(135)
        t.fd(boxf/15)
        ghost(x+boxf/2+boxf/15, y+boxf/2+boxf/4.5)
        
        
    #draw difference shape
    if "1" in mostsim[2]:
        ghost(x+boxf/2-.3*boxf, y+boxf/2)
        t.setheading(45)
        t.fd(boxf*.1)
    if "2" in mostsim[2]:
        ghost(x+boxf/2-.3*boxf, y+boxf/2)
        t.setheading(90)
        t.fd(boxf*.1)
    if "3" in mostsim[2]:
        ghost(x+boxf/2-.3*boxf, y+boxf/2)
        t.setheading(135)
        t.fd(boxf*.1)
    if "4" in mostsim[2]:
        ghost(x+boxf/2-.3*boxf, y+boxf/2)
        t.setheading(225)
        t.fd(boxf*.1)
    if "5" in mostsim[2]:
        ghost(x+boxf/2-.3*boxf, y+boxf/2)
        t.setheading(270)
        t.fd(boxf*.1)
    if "6" in mostsim[2]:
        ghost(x+boxf/2-.3*boxf, y+boxf/2)
        t.setheading(315)
        t.fd(boxf*.1)
    if "7" in mostsim[2]:
        ghost(x+boxf/2-.3*boxf, y+boxf/2)
        t.setheading(45)
        t.fd(boxf*.1)
        ghost(x+boxf/2-.3*boxf, y+boxf/2)
        t.setheading(225)
        t.fd(boxf*.1)
    if "8" in mostsim[2]:
        ghost(x+boxf/2-.3*boxf, y+boxf/2)
        t.setheading(90)
        t.fd(boxf*.1)
        ghost(x+boxf/2-.3*boxf, y+boxf/2)
        t.setheading(270)
        t.fd(boxf*.1)
    if "9" in mostsim[2]:
        ghost(x+boxf/2-.3*boxf, y+boxf/2)
        t.setheading(135)
        t.fd(boxf*.1)
        ghost(x+boxf/2-.3*boxf, y+boxf/2)
        t.setheading(315)
        t.fd(boxf*.1)
    
    #draw species shape
    if mostsim[4] == 1:
        ghost(x+boxf/2+.3*boxf, y+boxf/2)
        t.setheading(135)
        t.fd(boxf*.1)
    if mostsim[4] == 2:
        ghost(x+boxf/2+.3*boxf, y+boxf/2)
        t.setheading(90)
        t.fd(boxf*.1)
    if mostsim[4] == 3:
        ghost(x+boxf/2+.3*boxf, y+boxf/2)
        t.setheading(45)
        t.fd(boxf*.1)
    if mostsim[4] == 4:
        ghost(x+boxf/2+.3*boxf, y+boxf/2)
        t.setheading(315)
        t.fd(boxf*.1)
    if mostsim[4] == 5:
        ghost(x+boxf/2+.3*boxf, y+boxf/2)
        t.setheading(270)
        t.fd(boxf*.1)
    if mostsim[4] == 6:
        ghost(x+boxf/2+.3*boxf, y+boxf/2)
        t.setheading(225)
        t.fd(boxf*.1)
    if mostsim[4] == 7:
        ghost(x+boxf/2+.3*boxf, y+boxf/2)
        t.setheading(135)
        t.fd(boxf*.1)
        ghost(x+boxf/2+.3*boxf, y+boxf/2)
        t.setheading(315)
        t.fd(boxf*.1)
    if mostsim[4] == 8:
        ghost(x+boxf/2+.3*boxf, y+boxf/2)
        t.setheading(90)
        t.fd(boxf*.1)
        ghost(x+boxf/2+.3*boxf, y+boxf/2)
        t.setheading(270)
        t.fd(boxf*.1)
    if mostsim[4] == 9:
        ghost(x+boxf/2+.3*boxf, y+boxf/2)
        t.setheading(45)
        t.fd(boxf*.1)
        ghost(x+boxf/2+.3*boxf, y+boxf/2)
        t.setheading(225)
        t.fd(boxf*.1)
        
    
    if new_pos == "a":
        t.circle(boxf/30, 180)

    if new_pos == "r":
        t.circle(boxf/30, 180)

    return 1
    
 
#MAIN

#lemmatizer: will make words like "faster" reduced to their lemma (fast)
wnlem = WordNetLemmatizer()

#bottom righthand corner of box
#x = -480
#y = 300
x = 20 - (WIDTH)/2
y = HEIGHT/2 - 100
box = 100
hbuf = 10
x = x + hbuf
count = -1
for word in pos_tags:

    #causes wrap-around if it hits margin.
    if x >= WIDTH- 2*x:
        x = 20 - (WIDTH)/2
        y = y - 150

    
    #if len(wn.synsets(word, pos="n")) == 0:
        #print("your word " + word + " is not in the corpus and was skipped")
        #continue
    count += 1
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    
    #adjust direction of writing
    t.setheading(0)
    
    #Check for different word types

    #determinants
    if word[1] == "DT":
        commonword = maxsim(word[0], pronounlist, "PRP")
        if commonword[1] == 1:
            pronouns(commonword[0], x, y, box, t)
        else:
            print("your word: " + word[0] + ", this is a determinant, which is omitted")
        continue

    #pronouns
    if word[1] == "PRP" or word[1] == "PRP$" or word[1] == "WDT" or word[1] == "WP":
        commonword = maxsim(word[0], pronounlist, "PRP")
        pronouns(commonword[0], x, y, box, t)
        x = x + hbuf + box
        continue

    #pronouns if misassigned:
    if (word[0] == "thou" or word[0] == "thy" or word[0] == "i" or word[0] == "thine"):
        pronouns(word[0], x, y, box, t)
        x = x + hbuf + box
        continue

    #adverbs
    if (word[1] == "EX" or word[1] == "MD" or word[1] == "PDT" or 
    word[1] == "RB" or word[1] == "RBR" or word[1] == "RBS" or word[1] == "WRB"):
        commonword_conj = maxsim(word[0], conjunctionlist, "CONJ")
        commonword_prep = maxsim(word[0], prepositionlist, "ADP")
        commonword_adv = maxsim(word[0], adverblist, "ADV")
        if commonword_adv[1] == 1:
            adverbs(commonword_adv[0], x, y, box, t)
        elif commonword_conj[1] == 1:
            conjunctions(commonword_conj[0], x, y, box, t)
        elif commonword_prep[1] == 1:
            prepositions(commonword_prep[0], x, y, box, t)
        else:
            noun(word[0], x, y, word[1])

        x = x + hbuf + box
        continue

    # check both conjunctions and prepositions, pick the more common one
    if word[1] == "IN":
        commonword_conj = maxsim(word[0], conjunctionlist, "CONJ")
        commonword_prep = maxsim(word[0], prepositionlist, "ADP")
        commonword_adv = maxsim(word[0], prepositionlist, "ADV")
        if commonword_conj[1] == 1:
            conjunctions(commonword_conj[0], x, y, box, t)
        elif commonword_prep[1] == 1:
            prepositions(commonword_prep[0], x, y, box, t)
        elif commonword_adv[1] == 1:
            adverbs(commonword_adv[0], x, y, box, t)
        else:
            conjunctions(commonword_conj[0], x, y, box, t)

        x = x + hbuf + box
        continue



    
    if word[1] == "CC":
        commonword_conj = maxsim(word[0], conjunctionlist, "CONJ")
        commonword_prep = maxsim(word[0], prepositionlist, "ADP")
        commonword_adv = maxsim(word[0], prepositionlist, "ADV")
        if commonword_conj[1] == 1:
            conjunctions(commonword_conj[0], x, y, box, t)
        elif commonword_prep[1] == 1:
            prepositions(commonword_prep[0], x, y, box, t)
        elif commonword_adv[1] == 1:
            adverbs(commonword_adv[0], x, y, box, t)
        else:
            conjunctions(commonword_conj[0], x, y, box, t)
            
        x = x + hbuf + box
        continue
    #Prepositions
    if (word[1] == "RP" or word[1] == "TO"): 
        commonword_conj = maxsim(word[0], conjunctionlist, "CONJ")
        commonword_prep = maxsim(word[0], prepositionlist, "ADP")
        commonword_adv = maxsim(word[0], adverblist, "ADV")
        if commonword_prep[1] == 1:
            prepositions(commonword_prep[0], x, y, box, t)
        elif commonword_conj[1] == 1:
            conjunctions(commonword_conj[0], x, y, box, t)
        elif commonword_adv[1] == 1:
            adverbs(commonword_adv[0], x, y, box, t)

        prepositions(commonword_prep[0], x, y, box, t)
        x = x + hbuf + box
        continue

    if (word[1] == "NN" or word[1] == "NNP" or word[1] == "NNS" or word[1] == "UH" or word[1] == "VB"
    or word[1] == "VBD" or word[1] == "VBG" or word[1] == "VBN" or word[1] == "VBP" or word[1] == "VBZ"
    or word[1] == "JJ" or word[1] == "JJR" or word[1] == "JJS" or word[1] == "MD"):
        lemword = word[0]
        if "V" in word[1] or word[1] == "MD":
            lemword = wnlem.lemmatize(word[0], pos="v")
            print(lemword)
        if "J" in word[1]:
            lemword = wnlem.lemmatize(word[0], pos="a")
        noun(lemword, x, y, word[1])
        x = x + hbuf + box
        continue


    x = x + box + hbuf

    # if word is not in any of the above categories, put a giant circle, fill with green
    #to mean "IDK"


s.exitonclick()
#turtle.done()