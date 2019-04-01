import pandas
colnames=['total','latitude','longitude']
data=pandas.read_csv('total-parking.csv', names=colnames)
fh=open('abc.txt','w')
for x in range (1,1359):
    for y in range(0,int(data.total[x])):
        fh.write('%s, %s\n' % (data.latitude[x],data.longitude[x]))
fh.close()