import math
def isPrime(numb):
    if numb>1:
        for x in range(2,math.floor(math.sqrt(numb)+1)):
            if numb%x == 0:
                return False
        return True
    else: return False

def twoSidedPrime(numb):
    leftpop=rightpop=numb
    while leftpop>0 and rightpop>0:
        if isPrime(leftpop) and isPrime(rightpop):
            rightpop=math.floor(rightpop/10)
            leftpop=int(str(math.floor(int(str(leftpop)[::-1])/10))[::-1])
            continue
        return False
    return True