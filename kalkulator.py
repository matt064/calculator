import logging
logging.basicConfig(level=logging.DEBUG)


def add_values():
    """dodawanie"""
    a = float(input("Podaj składnik 1: "))
    b = float(input("Podaj składnik 2: "))
    logging.info(f"Dodaję {a} i {b}")
    sum = a + b
    print("Wynik to ", sum)
    exit()

def subtraction_values():
    """odejmowanie"""
    a = float(input("Podaj składnik 1: "))
    b = float(input("Podaj składnik 2: "))
    logging.info(f"Odejmuję {a} i {b}")
    sum = a - b
    print("Wynik to ", sum)
    exit()

def multiplication_values():
    """mnozenie"""
    a = float(input("Podaj składnik 1: "))
    b = float(input("Podaj składnik 2: "))
    logging.info(f"Mnożę {a} i {b}")
    sum = a * b
    print("Wynik to ", sum)
    exit()

def division_values():
    """dzielenie"""
    a = float(input("Podaj składnik 1: "))
    b = float(input("Podaj składnik 2: "))
    logging.info(f"Dzielę {a} i {b}")
    sum = a / b
    print("Wynik to ", sum)
    exit()


if __name__ == "__main__":
    print("Podaj działanie, poslugując sie odpowiednią liczbą:\n 1 Dodawanie\n 2 Odejmowanie\n 3 Mnożenie\n 4 Dzielenie")
    user_choice = int(input("Podaj liczbę: "))
  
    while 0 < user_choice < 5:
        if user_choice == 1:
            add_values()
        if user_choice == 2:
            subtraction_values()
        if user_choice == 3:
            multiplication_values()
        if user_choice == 4:
            division_values()
    else: 
        exit()
    




