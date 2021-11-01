#!/usr/bin/env python3

from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(open("../../publications.md", encoding="utf8"), "html.parser")

#lines = open('citations.csv').read()
lines = open('citations.csv').readlines()[0:5]
lines = (s + "- " for s in lines)
lines = ''.join(lines)
lines

for sup in soup.find_all('div', id="citations"):
    sup.string = lines
    sup.unwrap()
    
with open("../../publications.md", "w") as file:
    file.write(str(soup))

#END
