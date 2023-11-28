sekwencja = input('podaj sekwencję')
dlugosc = len(sekwencja)
i = 0
while i < dlugosc:
    print(sekwencja[i])
    i += 1

# lub to samo łatwiej:
sekwencja = input('Podaj sekwencję: ')
for litera in sekwencja:
    print(litera)