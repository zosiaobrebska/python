# Program rozpoznający zasady purynowe i pirymidynowe

# Pobranie litery od użytkownika
litera = input('Podaj symbol zasady: ').upper()

# Sprawdzenie czy litera odpowiada zasadzie purynowej, czy pirymidynowej.
if litera == 'A' or litera == 'G':
    print(f'{litera} to zasada purynowa')
elif litera == 'C' or litera == 'T' or litera == 'U':
    print(f'{litera} to zasada pirymidynowa')
else:
    print(f'Podałeś {litera} - błędna litera')