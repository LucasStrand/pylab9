import math
import random
import zlib
import collections

with open('exempeltext.txt', 'r') as file:
    txt = file.read()

#print(txt)
byteArr = bytearray(txt, "UTF-8")
print(len(txt))
print(len(byteArr)) 
# I "UTF-8" så kan vissa symboler ta upp mer än en byte, exeple på detta kan ses med "ÅÄÖ" i koden ovanför
# detta gör att bytearrayen blir längre än stringen.

def makeHisto(byteArr):
    histoList = [0] * 256
    for i in byteArr:
        histoList[i] += 1
    
#    twoBytesSymbole = False
#    wichTwoByte = 0
#
#    for i in byteArr:
#
#        if twoBytesSymbole:
#            twoBytesSymbole = False
#            if wichTwoByte == 194:
#                histoList[i] += 1
#            elif wichTwoByte == 195:
#                histoList[i+64] += 1
#        else:
#            if i < 128:
#                histoList[i] += 1
#            elif i == 194:
#                twoBytesSymbole = True
#                wichTwoByte = 194
#            elif i == 195:
#                twoBytesSymbole = True
#                wichTwoByte = 195 """
    print(histoList)
    return histoList
    

def makeProb(histoList):
    probList = [0]*256
    n = 0

    for i in range(256):
        probList[i] += histoList[i]/len(byteArr)
        print(i, "has a chance of ", round(probList[i], 4))
        n += probList[i]

    print(n)
    return probList

def entropi(probList):
    probLen = len(probList)

    entropiValue = 0
    for i in range(probLen):
        if probList[i] !=0:
            entropiValue += probList[i] * math.log(1 / probList[i], 2)

    print(entropiValue)
    return entropiValue
#Around 4.595 bytes per character can we compress the byteArray. 
#If you only write all the characters in order and not use any other algoritmes.

            

histoList = makeHisto(byteArr)
probList = makeProb(histoList)
entropiValue = entropi(probList)

theCopy = byteArr.copy()
random.shuffle(theCopy)

copyComp = zlib.compress(theCopy)
byteArrComp = zlib.compress(byteArr)

print(len(copyComp)) #19822
print(len(byteArrComp)) #12848

#entropy = 4.595 
# använder inte statistical redundancy men optimala encodingen

#copyComp = 5.451 
# eftersom den är shufflead anänder inte statistical redundancy 
# och använder inte optimala encodingen eftersom den är större än entropy

#arrComp = 3.533
# använder statistical redundancy och optimala encodingen

t1 = """I hope this lab never ends beacause
        it is so incredibly thrilling!"""
t10 = t1*10

t1ByteArr = bytearray(t1, "UTF-8")
t10ByteArr = bytearray(t10, "UTF-8")
print(len(t1ByteArr)) #74
print(len(t10ByteArr)) #740

t1Comp = zlib.compress(t1ByteArr)
t10Comp = zlib.compress(t10ByteArr)
print(len(t1Comp)) #73
print(len(t10Comp)) #83

# The compression of t10Comp is jsut 10 bytes longer then t1Comp cuz statistical redundancy is justed 
# and just have to tell that its compressed the same thing 10 times.