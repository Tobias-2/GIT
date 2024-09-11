import sys
import logging

type = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

if type == "1":
    print("Podaj 2 liczby do dodania:")
    x, y = map(int, input().split())
    t = x + y
    print(f"Doadję {x} i {y}")
elif type == "2":
    print("Podaj 2 liczby do odejmowania:")
    x, y = map(int, input().split())
    t = x - y
    print(f"Odejmuje {y} od {x}")
elif type == "3":
    print("Podaj 2 liczby do mnożenia:")
    x, y = map(int, input().split())
    t = x * y
    print(f"Mnożę {x} razy {y}")
elif type == "4":
    print("Podaj 2 liczby do dzielenia:")
    x, y = map(int, input().split())
    t = x / y 
    print(f"Dzielę {x} przez {y}")

print(f"Wynik to: {t}")