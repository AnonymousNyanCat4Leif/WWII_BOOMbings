import csv
import math

def setup():
    infile = open('operations.csv', mode='r')
    #CSV-data læses
    reader = csv.DictReader(infile)
    #og konverteres til en liste:
    data = list(reader)


def getBobs():
    totalBombs = 0
    numberOfMissions = 0

    #for-løkken gennemløber hele datasættet
    for row in data:
        #Den kolonne der hedder "PlanetaryMassJpt" indeholde massen, målt i enheden "jupitermasser".
        #Hvis massen ikke findes i datasættet får m værdien '' (En tom streng).
        #Derfor er vi nødt til at undersøge om m har en gyldig værdi,
        #før vi tæller planeten med:
        if row['High Explosives'] != '':
            m = float(row['High Explosives'])
            numberOfMissions += 1
            totalBombs += m


        # # Nu kan gennemsnittet udregnes:
        # return totalBombs/numberOfMissions
cmd = ""

while not cmd.startswith('q'):
    cmd = input('Skriv en kommando > ')

    if cmd == 'header':
        print(reader.fieldnames)

    if cmd == 'avg Bombs':
        print(getBobs())
