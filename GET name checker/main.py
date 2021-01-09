f = open('new first names.txt','r')
firstNames = f.read().splitlines()
f.close()
f = open('new last names.txt','r')
lastNames = f.read().splitlines()
f.close()

f = open('old names.txt','r')
oldNames = f.read().splitlines()
f.close()

for i in range(0,len(firstNames)):
    while ' ' in firstNames[i]:
        firstNames[i] = firstNames[i][0:firstNames[i].find(' ')] + firstNames[i][firstNames[i].find(' ') + 1: len(firstNames[i])]

for i in range(0,len(lastNames)):
    while ' ' in lastNames[i]:
        lastNames[i] = lastNames[i][0:lastNames[i].find(' ')] + lastNames[i][lastNames[i].find(' ') + 1: len(lastNames[i])]

newNames = []

for i in range(0,len(firstNames)):
    newNames.append(firstNames[i] + ' ' + lastNames[i])

temp = []
for name in newNames:
    if name not in temp:
        temp.append(name)
newNames = temp
newNames.sort()


for name in newNames:
    if name not in oldNames:
        oldNames.append(name)

oldNames.sort()
out = ''
for name in oldNames:
    out = out + name + '\n'
out = out[0:len(out)-2]

f = open('output.txt','w')
f.write(out)
f.close()
