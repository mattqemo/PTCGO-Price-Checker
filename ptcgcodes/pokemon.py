import requests
from bs4 import BeautifulSoup
import csv


URL = 'https://www.professor-oak.com/qrcodes/CodePrices.asp'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
soup = soup.prettify()

newEntries = dict()
prevEntries = dict()

i = 0
while i < (len(soup) - 10):
    if soup[i:i + 7] == "TCGOSet":
        i = i + 6
        while soup[i] != '\n':
            i = i + 1
        i = i + 1
        while not soup[i].isalnum():
            i = i + 1
        title = ''
        while soup[i] != '<':
            title += soup[i]
            i = i + 1
        while soup[i] != '$':
            i = i + 1
        cost = ''
        while soup[i] != '<':
            cost += soup[i]
            i = i + 1
        newEntries[title.replace('\n','').strip()] = cost.replace('\n','').strip()

    i = i + 1

#write newEntries to newcodes.txt
currPrices = open("newcodes.txt","w")

for title in newEntries:
    currPrices.write(title)
    currPrices.write('\n')
    currPrices.write(newEntries[title])
    currPrices.write('\n')

currPrices.close()

#read prevEntries from oldcodes.txt
with open("oldcodes.txt") as f:
    i = 0
    for line in f:
        if i % 2 == 0:
            prevTitle = line.replace('\n','')
        else:
            prevCost = line.replace('\n','')
            prevEntries[prevTitle.strip()] = prevCost.strip()
        i = i + 1

for entry in prevEntries:
    if newEntries.get(entry) is None:
        print("Code deleted: ", entry)
        print("-------------------------------")
    elif prevEntries[entry] != newEntries[entry]:
        print("Price change: ", entry)
        print("Previous: ", prevEntries[entry])
        print("Current: ", newEntries[entry])
        print("-------------------------------")

#replace old codes with new codes
currPrices = open("oldcodes.txt","w")
for entry in newEntries:
    currPrices.write(entry)
    currPrices.write('\n')
    currPrices.write(newEntries[entry])
    currPrices.write('\n')
    if prevEntries.get(entry) is None:
        print("Code Added: ", entry)
        print("Price: ", newEntries[entry])
        print("-------------------------------")

currPrices.close()

print("-------CODE FILE UPDATED-------")





