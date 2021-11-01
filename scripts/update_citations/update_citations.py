#!/usr/bin/env python3

from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open("../../publications.md", encoding="utf8"), "html.parser")

#lines = open('citations.csv').read()
lines = open('citations.csv').read().splitlines()[0:5]
lines = ("- "+s+" citations\n" for s in lines)
lines = "\n\n"+''.join(lines)+"\n"
lines

result = soup.find(id="citations")
result.string.replace_with(lines)
    
with open("../../publications.md", "w") as file:
    file.write(str(soup))

#END
