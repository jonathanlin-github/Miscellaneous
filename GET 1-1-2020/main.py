def toList(bob):
    out = ''
    for name in bob:
        out = out + name + '\n'
    return out

f = open("first names.txt", "r")
firstNames = f.read()
firstNamesEdited = ''
for x in range(0,len(firstNames)):
    if firstNames[x:x+1] != ' ':
        firstNamesEdited = firstNamesEdited + firstNames[x:x+1]
firstNames = firstNamesEdited.splitlines()
f.close()

f = open('last names.txt', 'r')
lastNames = f.read()
lastNamesEdited = ''
for x in range(0,len(lastNames)):
    if lastNames[x:x+1] != ' ':
        lastNamesEdited = lastNamesEdited + lastNames[x:x+1]
lastNames = lastNamesEdited.splitlines()
f.close()

f = open('events.txt', 'r')
events = f.read().splitlines()
f.close()

f = open('first names.txt', 'r')
firstNames = f.read().splitlines()
f.close()

f = open('last names.txt', 'r')
lastNames = f.read().splitlines()
f.close()

for x in range(0,len(firstNames)):
    if ' ' in firstNames:
        firstNames[x] = firstNames[x][0:len(firstNames[x])-1]
for x in range(0,len(lastNames)):
    if ' ' in lastNames:
        lastNames[x] = lastNames[x][0:len(lastNames[x])-1]

fullNames = []
for x in range(0,len(firstNames)):
    fullNames.append(firstNames[x] + ' ' + lastNames[x])

singlesPlayers = []
doublesPlayers = []

for x in range(0,len(fullNames)):
    if 'Singles' in events[x]:
        singlesPlayers.append(fullNames[x])
    if 'Doubles' in events[x]:
        doublesPlayers.append(fullNames[x])


print('SINGLES')
for name in singlesPlayers:
    print(name)

print('\nDOUBLES')
for name in doublesPlayers:
    print(name)


f = open('name output.txt','w')
f.write(toList(singlesPlayers))

f.close()

print('')
print('')
print('SORTED')
fullNames.sort()
for name in fullNames:
    print(name)

print('')
print('')
print('EXPECTED MONEY OUTPUT')
print(str(len(singlesPlayers) * 10))
print(str(len(doublesPlayers) * 5))
print(len(fullNames))

