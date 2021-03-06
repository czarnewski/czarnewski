#!/bin/bash

####################
# Update Citations #
####################

cd ~/repos/czarnewski
git pull

cd scripts/update_citations

python3 ~/repos/webscraping/code/google_scholar/google_scholar.py
python3 ~/repos/czarnewski/scripts/update_citations/update_citations.py

git add .
git commit -m "$(echo 'updates citations ('`date +"%m-%d-%y-%T"`')')"
git push



#sed -z "s|<div id=\"citations\">.*</div>|<div id=\"citations\">\nMYTAG\n</div>|g" ~/repos/czarnewski/publications.md | sed -e "/MYTAG/r citations.csv" -e "//d" > temp.md 

