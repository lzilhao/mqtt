f1 = open('pubtimes.txt', 'r')
f2 = open('senttimes.txt', 'r')
f3 = open('subtimes.txt', 'r')
f4 = open('diff.txt', 'w')

#print(f1.readline().strip())

sentlist = [line.rstrip('\n') for line in f2]
#print(sentlist)
publist = [line.rstrip('\n') for line in f1]
#print(publist)
for i in range(0,len(publist)):
    print(float(publist[i]) - float(sentlist[i]))
    f4.write(str(float(publist[i]) - float(sentlist[i])) + '\n')
    if i%100 == 0:
        print('\n')
f4.close()
#print(float(publist[1]) - float(sentlist[1]))
