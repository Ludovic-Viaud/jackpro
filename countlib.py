"""
module servant a gérer les fichier de configuration du comptage
"""

import xml.etree.cElementTree as ET
from discret import discret
from sabot import Sabot

def load(path):
    """
    charge un fichier de config (xml) situé
    a l'adresse [path] et renvoie un dictio
    """

    result = {}
    tree = ET.parse(path)
    root = tree.getroot()
    for child in root.findall('card'):
        result[eval(child.attrib['value'])] = eval(child.text)
    decksRem = root.find('decksRem')
    result['decksRem_precision'] = eval(decksRem.find('precision').text)
    result['decksRem_mode'] = decksRem.find('mode').text
    trueCount = root.find('trueCount')
    result['trueCount_formula'] = trueCount.find('formula').text.strip()
    result['trueCount_precision'] = eval(trueCount.find('precision').text)
    result['trueCount_mode'] = trueCount.find('mode').text

    return result

def save(dictio, path):
    """
    sauvegarde le dictio sous forme de fichier de config (xml)
    a l'adresse [path]
    """
    pass

def valide(etree):
    """
    valide le etree
    """
    pass

def calcTrueCount(rawCount, decksRem, countStrat) :
    decksRem = discret(value = decksRem,
                      precision = countStrat['decksRem_precision'],
                      mode = countStrat['decksRem_mode'])
    trueCount = eval(countStrat['trueCount_formula'])
    trueCount = discret(value = trueCount,
                        precision = countStrat['trueCount_precision'],
                        mode = countStrat['trueCount_mode'])
    return trueCount

def analyze(countStratPath, nbCards):
    # init
    countStrat = load(countStratPath)
    sabot = Sabot()
    rawCount = 0
    rawResult = {'nb' : 0, 'trueCount' : {}}

    # boucle
    for x in range(nbCards):  # @UnusedVariable
        # init boucle
        card = sabot.draw()
        rawResult['nb'] += 1
        trueCount = calcTrueCount(rawCount = rawCount,
                                  decksRem = sabot.decksRem(),
                                  countStrat = countStrat)

        # TODO : enregistrement des resultats
        if trueCount not in rawResult['trueCount']:
            rawResult['trueCount'][trueCount] = {'nb' : 0, 'groups' : {}}
        rawResult['trueCount'][trueCount]['nb'] += 1
        if countStrat[card] not in rawResult['trueCount'][trueCount]['groups']:
            rawResult['trueCount'][trueCount]['groups'][countStrat[card]] = 0
        rawResult['trueCount'][trueCount]['groups'][countStrat[card]] += 1

        # fin de boucle
        rawCount += countStrat[card]
        if sabot.cutcarded() :
            sabot.shuffle()
            rawCount = 0

    # TODO : preparation des resultats
    result = {}
    for key, value in rawResult['trueCount'].items():
        result[key] = {}
        for groupKey, groupValue in value['groups'].items():
            liste = []
            for countKey, countValue in countStrat.items():
                if type(countKey) == int and countValue == groupKey:
                    liste.append(countKey)
            cardsInGroup = len(liste)
            if 10 in liste :
                cardsInGroup += 3
            for card in liste:
                result[key][card] = groupValue / cardsInGroup
                if card == 10:
                    result[key][card] *= 4
                result[key][card] /= value['nb']

    # return
    return result


if __name__ == "__main__" :
    result = analyze('count/standard.count.xml', 100000)
