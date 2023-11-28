# Tworzymy listę
kodony = ['AGA', 'CUC', 'ACU', 'AGA', 'UUG', 'AGA']
# Wyszukiwany kodon
kodon = 'AGA'
# Początek wyszukiwania
start = 0
# Poniższa pętla będzie się wykonywała dopóki zmienna
# kontynuuj bedzie miała wartość True
kontynuuj = True
while kontynuuj:
    # Jeżeli w łańcuchu, począwszy od indeksu start...
    if kodon in kodony[start:]:
        # kodon szukany jest od miejsca start
        # pobierany indeks wystąpienia szukanego kodonu
        indeks = kodony.index(kodon,start)
        # wydruk wyniku
        print(f"{kodon} znajduje się na pozycji {indeks}")
        # zmiana wartości start, kolejne szukanie będzie się
        # odbywało od miejsca, w którym znaleziono ostatnio kodon +1
        start = indeks + 1
    # Jeśli nie znaleziono kodonu...
    else:
        # Zmienna kontynuuj przyjmuje wartość False
        # i pętla nie wykonuje się kolejny raz
        kontynuuj = False


######################################
#Można też odwrócić ten proces, z listy utworzyć ciąg znaków.
# Służy do tego metoda join():
peptyd = 'His Phe Val Thr Lys Lys'
aminokwasy = peptyd.split()
print(aminokwasy)
separator = "-"
peptyd = separator.join(aminokwasy)
print(peptyd)

#Jest to trochę nieintuicyjne, ale metodę join() wywołujemy nie na
# liście, ale na ciągu znaków, który staje się separatorem.
# Powyżej utworzyliśmy zmienną separator, ale można pominąć ten krok:
peptyd = '-*-'.join(aminokwasy)
print(peptyd)