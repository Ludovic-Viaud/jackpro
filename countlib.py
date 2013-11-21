"""
module servant a gérer les fichier de configuration du comptage
"""

import xml.etree.cElementTree as ET
from discret import discret  # @UnusedImport
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
    trueCount_formula = trueCount.find('formula').text.strip()
    codeOut = []
    code =  "def calcTrueCount(rawCount, decksRem, countStrat) :" "\n"
    code += "    decksRem = discret(value = decksRem," "\n"
    code += "                  precision = countStrat['decksRem_precision']," "\n"
    code += "                  mode = countStrat['decksRem_mode'])" "\n"
    for line in trueCount_formula.split('\n'):
        code += "    " + line + "\n"
    code += "    trueCount = discret(value = trueCount," "\n"
    code += "                    precision = countStrat['trueCount_precision']," "\n"
    code += "                    mode = countStrat['trueCount_mode'])" "\n"
    code += "    return trueCount" "\n"
    code += "codeOut.append(calcTrueCount)"
    exec(code)
    result['trueCount_formula'] = codeOut[0]
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
        trueCount = countStrat['trueCount_formula'](rawCount = rawCount,
                                                    decksRem = sabot.decksRem(),
                                                    countStrat = countStrat)

        # enregistrement des resultats
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

    # preparation des resultats
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
    result = analyze('count/standard.count.xml', 1000000)
