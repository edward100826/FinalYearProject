import pandas
colnames=['address','land_use','longitude','latitude']
a=pandas.read_csv('residentbuy.csv', names=colnames, encoding='Big5')
fh=open('resident.txt','w')
b='住'
for i in range (0,1131):
    if b==a.land_use[i]:
        fh.write('%s, %s, %s\n' % (a.address[i],a.latitude[i],a.longitude[i]))
fh.close()