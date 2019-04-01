import requests

GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'
fh=open('使用率.txt','r')
fw=open('hi.txt','w')
lines = fh.readlines()
b = 1
for line in lines:
    if 'Name' in line:
        reduced=line.split()
        reduced.insert(1,'台北市')
        for i in reduced:
            if i in 'Name':
                reduced.remove(i)
            a=''.join(reduced)
            print(a)
            params = {
                'address': a,
                'sensor': 'false',
                'region': 'tw',
            }

            req = requests.get(GOOGLE_MAPS_API_URL, params=params)
            res = req.json()
            print(res['status'])

            result = res['results'][0]

            geodata = dict()
            geodata['lat'] = result['geometry']['location']['lat']
            geodata['lng'] = result['geometry']['location']['lng']
            geodata['address'] = result['formatted_address']

            print(b,'. {address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
            fw.write('%s, %s, %s\n' % (a,geodata['lat'],geodata['lng']))
            b+=1

fh.close()
fw.close()