# Shannon Entropy Calculator
import math
url = raw_input("URL: ")
url = list(url) #seperate each char
alphabet = list(set(url)) # list of symbols in the string

# calculate the frequency of each symbol in the string
freqList = []
for symbol in alphabet:
    ctr = 0
    for sym in url:
        if sym == symbol:
            ctr += 1
    freqList.append(float(ctr) / len(url))

# Shannon entropy
ent = 0.0
for freq in freqList:
    ent = ent + freq * math.log(freq, 2)

print 'Shannon entropy: %s' % -ent
