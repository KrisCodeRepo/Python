# import urllib
# import urllib.request
import json
# from bs4 import BeautifulSoup

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# counts = dict()
# for line in fhand:
#     print(line.decode().strip())
#     words = line.decode().strip()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)

# url = input('Enter -')
# html =  urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')

# tags = soup('a')
# for tag in tags:
#     print(tag.get('href',None))

input = '''
{
    "users": [
        {
            "status": {
                "text": "@jazzychad I just bought one .__.",
             },
             "location": "San Francisco, California",
             "screen_name": "leahculver",
             "name": "Leah Culver",
         }
         ]
}
'''

# import xml.etree.ElementTree as ET

# stuff = ET.fromstring(input)

# lst =stuff.findall('users/user')
# print('User Count:', len(lst))
# for item in lst:
#     print('Name: ',item.find('name').text)
#     print('Id:', item.find('id').text)
#     print('Attribute:', item.get('x'))
nfo = json.loads(input)
print(nfo['user']['name'])