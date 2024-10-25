#Lotto 6 aus 45
"""
#1
6 eindeutige Zahlen aus dem Bereich 1-45 werden eingegeben
Check eingegebene Zahlen:
 - wurden wirklich Zahlen eingegeben
 - sind die einzelnen Zahlen im Bereich 1-45
 - Duplikate entfernen
 - Wurden wirklich 6 eindeutige Zahlen eingegeben, ansonsten nochmals eingeben


1 2 3 4 5 6

1: 1
2: 1
-> das Zahl2 erneut eingeben
2: 3
3: 4
4: a
-> es wurde keine Zahl eingegeben; zahl4 erneut eingeben
4: 6
5: 7
6: 50
-> zahl ist außerhalb des Bereiches 1-45
6: 45

#2 gewinnerzahlen per zufall generieren -> random verwenden

"""

import random

def userZahlen():
    """
    6 eindeutige Zahlen werden eingegben/gecheckt und in Liste gespeichert
    :return: liste
    """
    userList = []
    cnt = 1

    # V1 Zahlen einzeln einlesen
    """
    while len(set(userList)) != 6:          #solange wir nicht 6 eindeutige Zahlen in userList haben, läuft die Schleife
        raw = input(f'Zahl{cnt}: >')        # str -> check ob .numeric

        #check ob raw eine zahl ist
        if raw.isnumeric():
            zahl = int(raw)

            #check ob zahl innerhalb 1-45 ist
            #if zahl >= 1 and zahl <=45:
            if zahl in range(1,46):
                #todo check ob zahl bereits in Liste ist
                #V1 genauso wie in zeile 52 nur statt range userList
                userList.append(zahl)
                cnt += 1

            else:
                print('Zahl ist außerhalb des Bereiches 1-45!')
                continue
        else:
            print('Es wurde keine Zahl eingegeben!')
            continue #-> wieder an schleifen beginn springen
    """

    #V2
    while len(set(userList)) != 6:
        userList = list(map(int, input(f'Zahlen (mit Leerzeichen getreent) eingeben: ').split(' ')))
        #map ist eine Funktion, die mit jedem Element aus der Liste (eingabe von input); eine Konvertierung zu int macht

    return set(userList)

def computerZahlen():
    """
    6 eindeutige Zahlen werden generiert und in Liste gespeichert
    :return: liste
    """
    # print(random.randint(1,5))
    # 1-45 und das 6x (keine Duplikate)
    #print(random.sample(population=range(1, 46), k=6))
    # print(random.sample(range(1,46), 6))
    return set(random.sample(population=range(1, 46), k=6))              #hier wird kein Set benötigt, weil sample keine Duplikate zulässt

def compare(cpuZahlen, meineZahlen):
    """
    Vergleich mit set().intersection -> wie viele Gemeinsamkeiten kommen vor (len)
    :param cpuZahlen: gezogenen COmputerzahlen
    :param meineZahlen: eingegeben Userzahlen
    :return: länge der gemeinsamkeiten
    """


cpuZahlen = computerZahlen()
print(f'Gezogenen Computerzahlen: {cpuZahlen}')

meineZahlen = userZahlen()
print(f'Unsere Zahlen: {meineZahlen}')

#todo Anzahl der Ziehungen einlesen und mit Fehlerbehandlung überprpüfen
#anz = 150



gewinn = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
print(gewinn, type(gewinn))

#todo schleife die 150x läuft (laut anz-Wert) und jedes Mal neue cpuZahlen generiert; check wie viele gleich sind
#todo innerhalb der Schleife check wie viele Zahlen richtig sind

richtig = len(meineZahlen.intersection(cpuZahlen))

#V1
if richtig == 0:
    gewinn[richtig] +=1
elif richtig == 1:
    gewinn[richtig] += 1
elif richtig == 2:
    gewinn[richtig] += 1
#... bis richtig==6

#V2
#gewinn[len(meineZahlen.intersection(cpuZahlen))] +=1


#gewinn Statistik ausgeben
for k, v in gewinn.items():
    print(f'{k}er: {v}')

print(f'Wir haben einen Lotto {len(meineZahlen.intersection(cpuZahlen))}er -> {meineZahlen.intersection(cpuZahlen)}')


