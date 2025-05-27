# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count: '))      # How many times to follow the link
position = int(input('Enter position: '))  # Position of the link (1-based)
last_name = None

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    # Get the tag at the specified position (convert to 0-based index)
    tag = tags[position - 1]
    url = tag.get('href', None)
    last_name = tag.text
    print("Retrieving:", url)
print(last_name)