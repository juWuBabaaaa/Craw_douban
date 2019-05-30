#coding: utf8
'''
Created on 2019年5月29日

@author: sx
'''
from bs4 import BeautifulSoup
import urllib2
import io

url = "https://movie.douban.com/subject/26425063/"
response = urllib2.urlopen(url)
soup = BeautifulSoup(response.read(), 'html.parser', from_encoding='utf-8')

for tag in soup.find_all('div', class_='related-info'):
    summary = tag.find('div').get_text()
with io.open("craw-douban.txt", 'w', encoding='utf-8') as d:
    d.write(summary)
