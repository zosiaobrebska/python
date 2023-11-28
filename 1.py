slowo = input('Podaj słowo: ').upper()
litera = input('Podaj literę: ').upper()

if litera in slowo:
    print(f"Litera '{litera}' znajduje się w słowie '{slowo}'")
else:
    print(f"Litera '{litera}' nie znajduje się w słowie '{slowo}'")