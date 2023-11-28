# Zmienna przechowująca informację, czy kontynuować działanie pętli
kontynuowac = True
# Pętla, działa dopóki zmienna kontynuować na wartość True
while kontynuowac:
    # Pobranie danych od użytkownika
    m_roztworu = float(input('Podaj masę roztworu [g]: '))
    m_substancji_rozpuszczonej = float(input('Podaj masę substancji rozpuszczonej [g]: '))
    # Obliczenia
    print(f"""
    masa roztworu:                 {m_roztworu:>5.2f}g
    masa substancji rozpuszczonej: {m_substancji_rozpuszczonej:>5.2f}g
    stężenie:                      {100*m_substancji_rozpuszczonej/m_roztworu:>5.2f}%
    """)
    # Po wykonaniu iteracji pytamy użytkownika, czy chce kontynuować
    decyzja = input("Czy chcesz kontynować? [T/N]")
    # Jeśli nie chce...
    if decyzja.upper() == 'N':
        kontynuowac = False
    # Jeśli chce
    else:
        print("\n______________________\n")

print("Koniec")