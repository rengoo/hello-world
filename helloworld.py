# This Program says hello
import random # Importiert Modul; Alternative ist from, womit man sich das Prefix spart
print('Hello')
myName = input("Eingabe?")

def caseselect(answer):
    if answer == 1: 
        return 'lol'
    elif answer == 2:
        return 'jolo'

def myfunctionawesomefunction():
    print("You have called me")

for i in range(5):
    print("Stinrg und Zahl" + str(i))

i = 0
while i < 15:
    # print("Noch mehr Zahlen" + str(i))
    i = i + 1
    print("Zufallszahl " + str(random.randint(1,10)))

myfunctionawesomefunction()
caseselect(1)
