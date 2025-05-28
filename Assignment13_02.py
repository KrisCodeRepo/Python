import json
import urllib.request

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
try:
    info = json.loads(data)
except:
    info = None
#print(info['comments'])
count = len(info['comments'])
temp = dict()
temp = info['comments']
sum = 0
#print('temp', info['comments'][0]['count'])

for result in temp:
    print('result', result['count'])
    sum += result['count']

print('Count:', count)
print('Sum:', sum)

