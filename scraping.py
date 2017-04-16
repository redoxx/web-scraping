# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 00:47:07 2017

@author: REd
"""
from lxml import etree
import urllib

# The url pattern is http://www.societe.com/etablissement/FIRM_NAME-SIRET.html
url = "http://www.societe.com/etablissement/ventes-privees-43431729300018.html"
htmlfile = urllib.urlopen(url)
htmltxt = htmlfile.read()
html = etree.HTML(htmltxt)
## Get all 'tr'
tr_nodes = html.xpath('//table[@id="etab"]/tr')
## 'th' is inside first 'tr'
#header = [i[0].text for i in tr_nodes[0].xpath("th")]
## Get text from rest all 'tr'
td_content = [[td.text for td in tr.xpath('td')] for tr in tr_nodes[1:]]
      
for d in td_content:
    print d