"""
jackpro.py
logiciel de blackjack
"""

from sabot import Sabot
import countlib

def analyze(countStratPath, nbCards):
    countStrat = countlib.load(countStratPath)
    sabot = Sabot(6, 52)
    rawCount = 0
    trueCount = 0
    rawResult = {}
    rawResult['sabot'] = {}
    rawResult['sabot']['nb'] = 0
    for x in range(nbCards):
        card = sabot.draw()
        rawResult['sabot']['nb'] += 1
        trueCount = countlib.calcTrueCount(rawCount,
                                           sabot.cardsOut(),
                                           countStrat)
        if trueCount not in rawResult['sabot']:
            rawResult['sabot'][trueCount] = {'nb' : 0}
        rawResult['sabot'][trueCount]['nb'] += 1
        if card not in rawResult['sabot'][trueCount]:
            rawResult['sabot'][trueCount][card] = 0
        rawResult['sabot'][trueCount][card] += 1
        
        rawCount += countStrat[card]
        
        if sabot.cutcard() :
            sabot.shuffle()
            rawCount = 0
    
    return rawResult

if __name__ == "__main__" :
    result = analyze('standard.count.xml', 1000000)
