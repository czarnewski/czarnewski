#!/usr/bin/env python3
from optparse import OptionParser
from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open("~/repos/czarnewski/publications.md", encoding="utf8"), "html.parser")

#lines = open('citations.csv').read()
lines = open('~/repos/czarnewski/scripts/update_citations/citations.csv').read().splitlines()[0:5]
lines = ("- "+s+" citations\n" for s in lines)
lines = "\n\n"+''.join(lines)+"\n"
lines

result = soup.find(id="citations")
result.string.replace_with(lines)
    
with open("~/repos/czarnewski/scripts/update_citations/publications.md", "w") as file:
    file.write(str(soup))

#END
