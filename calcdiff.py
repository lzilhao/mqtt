import statistics

f1 = open('pubtimes.txt', 'r')
f2 = open('senttimes.txt', 'r')
#f3 = open('subtimes.txt', 'r')
f4 = open('diff.txt', 'w')

#print(f1.readline().strip())

sentlist = [line.rstrip('\n') for line in f2]
#print(sentlist)
publist = [line.rstrip('\n') for line in f1]
#print(publist)
#res = [len(publist)]
res = []
length = 1

for i in range(0, len(publist)):
    res.append(float(publist[i]) - float(sentlist[i]))
    #print(float(publist[i]) - float(sentlist[i]))
    if (i+1)%100 == 0:
        length *= 10
        print(str(length))
        print("     mean - " + str(statistics.mean(res)))
        print("     stdev - " + str(statistics.stdev(res)))
        del res[:]
f4.close()


#print(float(publist[1]) - float(sentlist[1]))
