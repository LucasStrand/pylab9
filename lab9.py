import math
import random
import zlib
import collections

with open('exempeltext.txt', 'r') as file:
    txt = file.read()

byteArr = bytearray(txt, "UTF-8")
print(len(txt))
print(len(byteArr))
#How many symbols does the string contain? How many bytes does the byte-array contain? Explain differences.
# In UTF-8 some characters such as "Å,Ä,Ö" can contain more than one byte and therefore the bytearray is longer than the string

def makeHisto(byteArr):
    histo = [0] * 256
    for i in byteArr:
        histo[i] += 1

    print(histo)
    return histo
    

def makeProb(histo):
    prob = [0]*256
    n = 0

    for i in range(256):
        prob[i] += histo[i]/len(byteArr)
        print(i, "has a chance of ", round(prob[i], 4))
        n += prob[i]

    print(n)
    return prob

def entropi(prob):
    probLen = len(prob)

    entropiValue = 0
    for i in range(probLen):
        if prob[i] !=0:
            entropiValue += prob[i] * math.log(1 / prob[i], 2)

    print(entropiValue)
    return entropiValue

#Down to how many bytes should it be possible to compress the byte-array byteArr if we treat it as a memory source (i.e., we do not exploit
# #statistical redundancy) but use an optimal encoding?

#If all the characters are written in order and not using any other algorithms,
#we are able to compress the byteArr to about 4.64 bytes per char

            

histo = makeHisto(byteArr)
prob = makeProb(histo)
entropiValue = entropi(prob)

theCopy = byteArr.copy()
random.shuffle(theCopy)

copyComp = zlib.compress(theCopy)
byteArrComp = zlib.compress(byteArr)

print(len(copyComp))
#23061
print(len(byteArrComp))
#13060

#entropy = 4.64
#doesnt use statistical redundancy, but the optimal encoding

#copyComp = 5.451 
#shuffled therefore doesn't use statistical redundancy
#since it's bigger than the entropy, it is not using optimal encoding

#arrComp = 3.533
#uses both statistical redundancy and optimal encoding

t1 = """I hope this lab never ends beacause
        it is so incredibly thrilling!"""
t10 = t1*10

t1ByteArr = bytearray(t1, "UTF-8")
t10ByteArr = bytearray(t10, "UTF-8")
print(len(t1ByteArr)) #74
print(len(t10ByteArr)) #740

t1Comp = zlib.compress(t1ByteArr)
t10Comp = zlib.compress(t10ByteArr)
print(len(t1Comp)) #72
print(len(t10Comp)) #82

#No it doesnt become 10 times bigger compressed but however adds 10 bytes. The compilation
#recognizes that it is just the same text 10 times over (t10 = t1*10)