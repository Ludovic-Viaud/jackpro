"""
module permetant d'arrondir selon plusieur mode et plusieurs precisions
"""

import math

def discret(value, precision=1, mode="auto") :
    if precision not in [1, 2, 4, 5, 8, 10]:
        raise ValueError('precision doit etre 1, 2, 4, 5, 8 ou 10')
    if mode not in ['auto', 'trunc', '-trunc', 'floor', 'ceil']:
        raise ValueError('mode doit etre "auto", "tronc", "-tronc", "floor", "ceil"')
    if precision == 0 :
        return value
    if value == 0 :
        return 0
    if mode == 'auto' :
        result = round(value*precision)/precision
    elif mode == "trunc" :
        result = int(value*precision)/precision
    elif mode == "-trunc" :
        temp = int(value*precision)
        temp += temp >= 0 and 1 or -1
        result = temp/precision
    elif mode == "floor" :
        result = math.floor(value*precision)/precision
    elif mode == "ceil" :
        result = math.ceil(value*precision)/precision

    return result

def texte_discret(var, precision=1, mode='auto'):
    if precision not in [1, 2, 4, 5, 8, 10]:
        raise ValueError('precision doit etre 1, 2, 4, 5, 8 ou 10')
    if mode not in ['auto', 'trunc', '-trunc', 'floor', 'ceil']:
        raise ValueError('mode doit etre "auto", "tronc", "-tronc", "floor", "ceil"')
    code =  ""
    if mode == 'auto' :
        code += "%s = round(%s*%s)/%s" % (var, var, precision, precision) + "\n"
    elif mode == "trunc" :
        code += "%s = int(%s*%s)/%s" % (var, var, precision, precision) + "\n"
    elif mode == "-trunc" :
        code += 'temp = int(%s*%s)' % (var, precision) + "\n"
        code += 'temp += temp >= 0 and 1 or -1' + "\n"
        code += '%s = temp/%s' % (var, precision) + "\n"
    elif mode == "floor" :
        code += "%s = math.floor(%s*%s)/%s" % (var, var, precision, precision) + "\n"
    elif mode == "ceil" :
        code += "%s = math.ceil(%s*%s)/%s" % (var, var, precision, precision) + "\n"

    return code.strip().split('\n')

if __name__ == "__main__" :
    pass
