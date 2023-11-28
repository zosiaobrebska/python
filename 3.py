## Mini gra przygodowa:

imie = input("Jesteś wojownikiem, który znalazł się w ciemnym lesie, który ludzie nazywają " +
             "Smoczym Lasem. \nPodaj swoje imię: ")
sciezka = input(f"{imie}, stoisz na ścieżce, która się rozwidla, gdzie idziesz?\n" +
                "p - w prawo, l - w lewo: ")
if sciezka == 'l':
    wybor = input("Widzisz wejście do jaskini. Wchodzisz?\n" +
                   "tak - t, nie - n :")
    if wybor == 't':
        print(f"{imie}! Znalazłeś skarb!")
    elif wybor == 'n':
        print("Szkoda...")
    else:
        print("Nie ma takiej opcji.")
elif sciezka == 'p':
    wybor = input("Widzisz wielką smoczycę. Co robisz?\n" +
                   "w - walczę, u - uciekam: ")
    if wybor == 'w':
        print(f"{imie}! To nie jest najlepszy pomysł napadać na smoczycę z gołymi rękami. " +
              "Smoczyca Cię zjadła!")
    elif wybor == 'u':
        wybor = input("Ocaliłeś życie. Natykasz się na małego smoczka. Co robisz?\n" +
                     "o - oddaję smoczycy, b - biorę do domu, z - zostawiam w spokoju: ")
        if wybor == 'o':
            print("Smoczyca jest zachwycona, w nagrodę daje Ci worek złota.")
        elif wybor == 'b':
            imie_smoka = input("Zabrałeś smoka do domu. Ciekawe, czy to dobry pomysł? " +
                               "Jak dałeś mu na imię?\n")
            print(f"Smok {imie_smoka} rósł w Twoim domu, towarzysząc Ci w codziennym życiu.\n" +
                 "Jednak pewnego dnia, kiedy zapomniałeś go nakarmić, zjadł Cię " +
                 "i odleciał do smoczego lasu. \n" +
                 "Morał: nie zabieraj ze sobą dzikich zwierząt.")
        elif wybor == 'z':
            print("Mądry wybór, choć może coś Cię ominęło?")
        else:
            print("Nie ma takiej opcji.")
    else:
        print("Nie ma takiej opcji. Niestety, smoczyca nie czekała na własciwą decyzję" +
              "i Cię zjadła.")
else:
    print("Nie ma takiej ścieżki.")
print("Koniec przygody.")