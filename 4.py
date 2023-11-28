i = 1
while i <= 19:
    print(f"{i*'*': ^19}") #19 bo w ostatniej linii jest 19 *
    i += 2


#lub z łodyga:
i = 1
print(f"{i*'*': ^21}")
while i <= 10:
    print(f"{i*'*': >10}|{i*'*': <10}")
    i += 1