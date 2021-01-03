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

fullNames = []
for x in range(0,len(firstNames)):
    fullNames.append(firstNames[x] + ' ' + lastNames[x])

f = open('name output.txt','w')
fullNames.sort()
fullNamesList = []
out = ''
totalPlayerCount = 0
for name in fullNames:
    out = out + name + '\n'
    totalPlayerCount = totalPlayerCount+1
    fullNamesList.append(name)
#f.write(out)
#f.write('\n'+'Total players: ' + str(totalPlayerCount))

singlesPlayers = []
doublesPlayers = []

ff = open('events.txt','r')
events = ff.read().splitlines()
for x in range(0,len(fullNamesList)) :
    if 'Singles' in events[x]:
        singlesPlayers.append(fullNamesList[x])
    if 'Doubles' in events[x]:
        doublesPlayers.append(fullNamesList[x])
ff.close()

singlesPlayersCount = 0
#f.write('\n')
#f.write('\n')
#f.write('singles')
#f.write('\n')
for name in singlesPlayers:
    #f.write(name+'\n')
    singlesPlayersCount = singlesPlayersCount + 1

doublesPlayersCount = 0
#f.write('\n')
#f.write('\n')
#f.write('doubles')
#f.write('\n')
for name in doublesPlayers:
    #f.write(name+'\n')
    doublesPlayersCount = doublesPlayersCount + 1

#for name in fullNamesList:

out = 'Total players: ' + str(len(fullNamesList)) + '\n' + 'Singles Players: ' + str(len(singlesPlayers)) + '\n' + 'Doubles Players: ' + str(len(doublesPlayers)) + '\n'

out = out + '------------------------' + '\n'
out = out + 'SINGLES' + '\n\n'
for name in singlesPlayers:
    out = out + name + '\n'
out = out + '\n' + '-----------------------' + '\n'
out = out + 'DOUBLES' + '\n\n'
for name in doublesPlayers:
    out = out + name + '\n'

f.write(out)
