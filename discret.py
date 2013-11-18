"""
module permetant d'arrondir selon plusieur mode et plusieurs precisions
"""

def discret(value, precision=1, mode="auto") :
    if precision == 0 : return value
    if value == 0 : return 0
    value = float(value)
    if mode == 'auto' :
        temp = value/precision
        tempint = int(temp)
        result = (tempint + int(round(temp-tempint)))*precision
    elif mode == "trunc" :
        result = int(value/precision)*precision
    elif mode == "-trunc" :
        result = int(value/precision)*precision
        result += result >= 0 and precision or -precision
    elif mode == "floor" :
        result = int(value/precision)*precision
        if result < 0 :
            result -= precision
    elif mode == "ceil" :
        result = int(value/precision)*precision
        if result >= 0 :
            result += precision
    else :
        raise Exception('%s is not a valide mode' % mode)
    
    return result

if __name__ == "__main__" :
    pass
