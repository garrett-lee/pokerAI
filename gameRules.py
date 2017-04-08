#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
#import numpy as np
from collections import Counter

mapping = {0:"2C", 1:"3C", 2:"4C", 3:"5C", 4:"6C", 5:"7C", 6:"8C", 7:"9C", 8:"10C", 
           9:"JC", 10:"QC", 11:"KC", 12:"AC", 13:"2D", 14:'3D',15:'4D',16:'5D',17:'6D',
           18:'7D',19:'8D', 20:'9D', 21:'10D', 22:'JD', 23:'QD', 24:'KD', 25:'AD',
           26:'2H', 27:'3H', 28:'4H',29:'5H', 30:'6H', 31:'7H', 32:'8H', 33:'9H',
           34:'10H',35:'JH',36:'QH',37:'KH',38:'AH',39:'2S',40:'3S',41:'4S',42:'5S',
           43:'6S', 44:'7S', 45:'8S', 46:'9S', 47:'10S', 48:'JS', 49:'QS', 50:'KS', 51:'AS'}

mapping2 = {0: 'two', 1: 'three', 2:'four', 3:'five', 4:'six', 5:'seven', 6:'eight',
            7:'nine', 8:'ten', 9:'jack', 10:'queen', 11:'king', 12:'ace'}

#royal flush
cards = range(0,52)
handx = random.sample(cards, 5)
handMap = [mapping[x] for x in handx]

def checkHand(hand):
    hand = sorted(hand)
    card1 = hand[0]
    card2 = hand[1]
    card3 = hand[2]
    card4 = hand[3]
    card5 = hand[4]
    
    moddedHand = [x%13 for x in hand]
    counts = Counter(moddedHand).most_common()
    
    #we need all the cards to be in a sequential order and mod13==8,9,10,11, and 12
    if (card1==card2-1==card3-2==card4-3==card5-4) and card1%13==8 and card2%13==9 and card3%13==10 and card4%13==11 and card5%13==12:
        print("Royal flush!")
    #we need to check sequentiality of normal cards and their mods are sequential
    elif (card1==card2-1==card3-2==card4-3==card5-4) and (card1%13==card2%13-1==card3%13-2==card4%13-3==card5%13-4):
        print("Straight flush!")
    elif counts[0][1] == 4:
        print("4 of a kind with " + mapping2[counts[0][0]] + "s")
    elif counts[0][1] == 3 and counts[1][1] == 2:
        print("Full house with "+mapping2[counts[0][0]]+"s and "+mapping2[counts[1][0]]+"s")
    
        
    
y = [2,15,28,17,4]
checkHand(y)