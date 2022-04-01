# Funktion in Funktion

def outer(func):
    cached = {}     # ein Dictionary erstellen
    def inner(x):   # Funktion checkt ob es zu parameter x bzw 5,gibt ein gecached Wert in Dictionary
        if x in cached:
            return cached[x]    # wenn ja, gibts der Wert aus
        result = func(x) # wenn nicht dann ruft die untere Funktion
        cached[x] = result  # und speichert in Dictionary
        return result   # und wird das Ergebnis zurückgeben

    return inner

@outer      # das ist decorator, er wird untere Funktion ignorieren bzw ersetzen mit outer Funktion von oben
def calculate_something(x):
    print("calculate_something(" + str(x) + ")")
    return x * x

print(calculate_something(5))


##################################################################################


def repeat(n):  # 2
    def deco(func): # 3
        def inner():    # 4
            for i in range(0, n):
                func()

        return inner
    return deco

@repeat(5)  # 1
def do_something(): # 5
    print("do_something() wurde ausgeführt")    # 6

do_something()


