"""
module servant a gérer les fichier de configuration du comptage
"""

import xml.etree.cElementTree as ET
from discret import discret

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
    sabot = root.find('sabot')
    result['sabot_precision'] = eval(sabot.find('precision').text)
    result['sabot_mode'] = sabot.find('mode').text
    trueCount = root.find('trueCount')
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

def calcTrueCount(rawCount, cardsOut, countStrat) :
    nbDecks = discret(6-(cardsOut/52.),
                      precision = countStrat['sabot_precision'],
                      mode = countStrat['sabot_mode'])
    trueCountTemp = float(rawCount) / nbDecks
    trueCount = discret(trueCountTemp,
                        precision = countStrat['trueCount_precision'],
                        mode = countStrat['trueCount_mode'])
    return trueCount

if __name__ == "__main__" :
    countStrat = load('nocount.count.xml')
