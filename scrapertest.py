html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

##BS4 constructor
from bs4 import BeautifulSoup

##HTTp requests library
import requests

url = "https://rivalstracker.com/profile/1131824006"
page = requests.get(url)

parsedPage = BeautifulSoup(page.text, 'html.parser')

print(parsedPage)
