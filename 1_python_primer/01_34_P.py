print("""
A common punishment for school children is to write out a sentence multiple times.
Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.
""")

from random import choice

ms = set()
letters = list(map(chr, range(97, 123)))
typos = set()
sentence = "I will never spam my friends again"

while len(ms) < 8:    
    ms.add(choice(range(0,99)))

while len(typos) < 8:    
    pos = choice(range(0, len(sentence)))
    mistake = choice(letters)
    
    if sentence[pos] != mistake:
        sentwtypo = list(sentence)
        sentwtypo[pos] = mistake
        typos.add("".join(sentwtypo))

for i in range(0,100):
    writeout = sentence if i not in list(ms) else typos.pop()
    print("{0} - {1}.".format(format(i, '02d'), writeout))

print("\nSentences with typos: {0}".format(sorted(list(ms))))

    

 
        
    




