#!/bin/bash

####################
# Update Citations #
####################

cd ~/repos/czarnewski
git pull

cd scripts/update_citations

python3 ~/repos/webscraping/code/google_scholar/google_scholar.py
python3 update_citations.py

git add .
git commit -m "$(echo 'updates citations ('`date`')')"
git push



#sed -z "s|<div id=\"citations\">.*</div>|<div id=\"citations\">\nMYTAG\n</div>|g" ~/repos/czarnewski/publications.md | sed -e "/MYTAG/r citations.csv" -e "//d" > temp.md 

