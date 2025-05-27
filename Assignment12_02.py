#https://py4e-data.dr-chuck.net/comments_42.html
import urllib
import urllib.request

from bs4 import BeautifulSoup
url = input('Enter -')
html =  urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
#print(tags)
sum = 0
for tag in tags:
    #print(tag.text)
    if sum == 0:
        sum += int(tag.text)
    else:
        sum += int(tag.text)
print(sum)
    #print(tag.get('class="comments"',None))