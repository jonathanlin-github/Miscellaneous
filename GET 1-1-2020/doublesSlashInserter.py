f = open('doublesnames1.txt','r')
first = f.read().splitlines()
f.close()

f = open('doublesnames2.txt','r')
second = f.read().splitlines()
f.close()

for x in range(0,len(second)):
    print(first[x]+'/'+second[x])