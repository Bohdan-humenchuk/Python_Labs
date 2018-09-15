import random

file = open('text.txt', 'w')
testlist=[]
for i in range(0, 20):
    testlist.append(random.randint(0, 174))
print(testlist)
for elem in testlist:
    file.write(str(elem)+'\n')
file.close()

##############

fileA = open('a.txt', 'w')

fileA.write("Beside the hut the cherries are in bloom, \n"+
"And May bugs o'er them dance The peasants from \n"+
"The fields return with weary seep 'Tis late \n"+
"The young maids as they go sing songs At home \n"+
"The tables have been laid, and supper waits. \n"+

"A family at table sit without \n"+
"Dusk slowly comes, the evening stars are out. \n"+
"The daughter serves, but seems to take too long; \n"+
"The mother is impatient and about \n"+
"To scold, when lo! - a bird bursts into song. \n"+

"The darkness cloaks the heavens overhead... \n"+
"Beside the hut her little ones to bed \n"+
"The mother puts, and then, afraid that they'll \n"+
"Not sleep, lies down nearby \n"+
"The world seems dead \n"+
"All's still save for the maids and nightingale. \n")

fileA.close()

###############

fileA = open('a.txt', 'r')
fileB1 = open('b1.txt', 'w')
fileB2 = open('b2.txt', 'w')

virsh=[]
for line in fileA:
    virsh.append(line)

for i in range(0, len(virsh), 2):
    fileB1.write(virsh[i].upper())
    fileB2.write(virsh[i+1].lower())    

fileA.close()
fileB1.close()
fileB2.close()


mastemp=[]
mas4=[]
fileA = open('a.txt', 'r')
for line in fileA:
    mastemp.append(line.split(' '))
for a in mastemp:
    for b in a:
        if (b!='\n'):
            mas4.append(b.lower())
print(mas4)



import xml.etree.ElementTree as ET

root=ET.Element('root')




