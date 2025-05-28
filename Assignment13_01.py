import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
sum = 0
for result in counts:
    print(result.text)
    sum +=int(result.text)

print('Count:', len(counts))
print('Sum:', sum)

