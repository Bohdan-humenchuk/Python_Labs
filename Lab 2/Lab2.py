import random
import re
import io
import xml.etree.ElementTree as ET
import collections



file = open('text.txt', 'w')
testlist=[random.randint(0, 174)  for _ in range(20)]

#for i in range(0, 20):
 #   testlist.append(random.randint(0, 174))
print(testlist)
for elem in testlist:
    file.write(str(elem)+'\n')
file.close()

##############

fileA = open('a.txt', 'w')

fileA.write("Beside the hut the cherries are in bloom , \n"+
"And May bugs o'er them dance The peasants from \n"+
"The fields return with weary seep 'Tis late \n"+
"The young maids as they go sing songs At home \n"+
"The tables have been laid, and supper waits . \n"+

"A family at table sit without \n"+
"Dusk slowly comes , the evening stars are out . \n"+
"The daughter serves , but seems to take too long ; \n"+
"The mother is impatient and about \n"+
"To scold, when lo ! - a bird bursts into song . \n"+

"The darkness cloaks the heavens overhead ... \n"+
"Beside the hut her little ones to bed \n"+
"The mother puts , and then , afraid that they'll \n"+
"Not sleep , lies down nearby \n"+
"The world seems dead \n"+
"All's still save for the maids and nightingale . \n")

fileA.close()

###############

fileA = open('a.txt', 'r')
fileB1 = open('b1.txt', 'w')
fileB2 = open('b2.txt', 'w')

virsh=[]
for line in fileA:
    print(line)
    virsh.append(line)

for i in range(0, len(virsh), 2):
    fileB1.write(virsh[i].upper())
    fileB2.write(virsh[i+1].lower())    

fileA.close()
fileB1.close()
fileB2.close()

import collections

mastemp=[]
mas4=[]
fileA = open('a.txt', 'r')
for line in fileA:
    mastemp.append(line.split(' '))
for a in mastemp:
    for b in a: 
        if (b!='\n' and b!='!' and b!='-' and b!='...' and b!=',' and b!='.' and b!=';'):
            mas4.append(b.lower())
            counter=collections.Counter(w.strip() for w in mas4)

ends = re.findall(r'..\w\b', str(mas4))
print(ends)

root = ET.Element("root")
data1 = ET.SubElement(root, "data1")
data2 = ET.SubElement(root, "data2")
for key in counter:
    ET.SubElement(data1, "word", name=key).text = str(counter[key])

ET.dump(root)
tree=ET.ElementTree(root)
tree.write("X.xml")

##a = io.open('a.txt', 'r', newline='\n')
##words = re.findall(r'[а-яієї’А-Я]*[а-яієї’А-Я]\b',a.read())
##d = dict()
##for i in words:
##       if i not in d:d[i] = 1
##       else:d[i] += 1
##import xml.etree.cElementTree as ET
##
##root = ET.Element("root")
##data = ET.SubElement(root, "data")
##word = ET.SubElement(data,"word")               
##ends = re.findall(r'..\w\b', str(words))
##print(ends)
##e = dict()
##for end in ends:
##      if end not in e:e[end] = 1
##      else:e[end] += 1
##wordsinline = {}
##k = 0
##for line in lines:
##    line = line.split()
##    wordsinline[k]= len(line)
##    k+=1
##k = 0
##wordit = 1
##lineit = 0
##for i in ends:
##        word = ET.SubElement(data, "word")
##        ET.SubElement(word, "word", name=str(words[k])).text = str(d[words[k]])
##        ET.SubElement(word, "end", name=str(i)).text = str(e[i])
##        ET.SubElement(word, "stringnumber").text = str(lineit+1)
##        ET.SubElement(word, "wordnumber").text = str(wordit)
##         
##        if wordit >= wordsinline[lineit]:
##            lineit+=1
##            wordit = 1
##        else:
##            wordit +=1
##        k+=1
##    
##tree = ET.ElementTree(root)
##tree.write("c.xml")


