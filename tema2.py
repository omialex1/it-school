# 21) Sa se numere de cate ori apare o litera intr-un cuvant. (folositi for si while)
# 22) Sa se afiseze toate numerele pare pana la 100.
# 23) Sa se afiseze toate numerele impare pana la 50.
# 24) Sa se afiseze toate puterile lui 2 mai mici decat 150.
# 25) Sa se afiseze toate toate puterile lui 3 cuprinse intre 200 si 300.
# 26) Se citeste un numar de la tastatura. Sa se calculeze suma numerelor de la 1 pana la numarul citit. (folositi for si while)
# 27) Se citeste un numar de la tastatura. Sa se calculeze produsul numerelor de la 1 pana la numarul citit. (folositi for si while)
# 28) Se citeste un numar n de la tastatura. Sa se scrie un program care face o numaratoare inversa de la numarul respectiv pana la 0.
# 29) Se citeste un numar de la tastatura. Sa se afiseze toti divizorii acestuia.
# 30) Se citeste un numar intreg de la tastatura. Sa se afiseze pe rand fiecare cifra a acestuia folosind un while.
# 31) Sa se scrie un program care genereaza un numar aleator intre 1 si 100
# (folositi modulul random cum am utilizat in sesiunile precedente).
# Utilizatorul trebuie sa ghiceasca numarul generat introducand variante de la tastatura.
# Programul trebuie sa ofere indicii utilizatorului daca nu ghiceste numarul (Exemplu: numarul generat e 29.
# Daca noi introducem valoarea 7, trebuie sa ne spuna ca e gresit si ca trebuie sa alegem un numar mai mare.
# Daca introducem valoarea 55, atunci trebuie sa ne spuna ca numarul generat este mai mic decat valoarea introdusa de noi)



# 21) Sa se numere de cate ori apare o litera intr-un cuvant. (folositi for si while)


# cuvant = "mamaliga"
#
# for litera_a in cuvant:
#     if litera_a == "a":
#         print(cuvant.count("a"))
#         break


# cuvant = "mamaliga"
# x = "a"
# while x in cuvant:
#     print(cuvant.count("a"))
#     break



# 22) Sa se afiseze toate numerele pare pana la 100.

# x = range(1,101)
# for numar in x:
#     if numar % 2 == 0:
#         print(numar)


# x = range(1,101)
# numar = 1
# while numar in x:
#     if numar % 2 == 0:
#         print(numar)
#     numar += 1



# 23) Sa se afiseze toate numerele impare pana la 50.

# for numar in range(1,50):
#     if numar % 2 == 1:
#         print(numar)

# x = range(1,50)
# # numar = 1
# # while numar in x:
# #     if numar % 2 == 1:
# #         print(numar)
# #     numar += 1



# 24) Sa se afiseze toate puterile lui 2 mai mici decat 150.

# x = 1
# for exponent in range(150):
#     if 2 ** x < 150:
#         print(2 ** x)
#     else:
#         break
#     x += 1



# 25) Sa se afiseze toate toate puterile lui 3 cuprinse intre 200 si 300.

# x = 1
# while True:
#     if 200 < 3 ** x < 300:
#         print(3 ** x)
#     x += 1



# 26) Se citeste un numar de la tastatura.
# Sa se calculeze suma numerelor de la 1 pana la numarul citit. (folositi for si while)

# x = int(input("Introduceti un numar: "))
# y = range(1,x)
# for element in y:
#     print(element + x)
#     if element > x:
#         break


# x = int(input("Introduceti un numar: "))
# y = 1
# while True:
#     print(x+1)
#     y += 1
#     if y >= x:
#         break



# 27) Se citeste un numar de la tastatura.
# Sa se calculeze produsul numerelor de la 1 pana la numarul citit. (folositi for si while)

# x = int(input("Introduceti un numar: "))
# # y = range(1,x)
# #
# # for suma in y:
# #     print(x*suma)


# x = int(input("Introduceti un numar: "))
# y = 1
# rez = y * x
#
# while True:
#     print(rez)
#     y += 1
#     if y > x:
#         break



# 28) Se citeste un numar n de la tastatura.
# Sa se scrie un program care face o numaratoare inversa de la numarul respectiv pana la 0.

# x = int(input("Introduceti un numar: "))
#
# while x >= 0:
#     print(x)
#     x -= 1



# 29) Se citeste un numar de la tastatura. Sa se afiseze toti divizorii acestuia.


# x = int(input("Introduceti un numar: "))
# y = 1
# while x % y == 0 and y <= x:
#     print(y)
#     y += 1



# 30) Se citeste un numar intreg de la tastatura. Sa se afiseze pe rand fiecare cifra a acestuia folosind un while.


# x = int(input("Introduceti un numar: "))
#
# while x >= 10:
#     for cifra in x:
#         print(cifra)



# 31) Sa se scrie un program care genereaza un numar aleator intre 1 si 100
#(folositi modulul random cum am utilizat in sesiunile precedente).
# Utilizatorul trebuie sa ghiceasca numarul generat introducand variante de la tastatura.
# Programul trebuie sa ofere indicii utilizatorului daca nu ghiceste numarul (Exemplu: numarul generat e 29.
# Daca noi introducem valoarea 7, trebuie sa ne spuna ca e gresit si ca trebuie sa alegem un numar mai mare.
# Daca introducem valoarea 55, atunci trebuie sa ne spuna ca numarul generat este mai mic decat valoarea introdusa de noi)


# from random import randint
#
# x= (randint(1,100))
# y = int(input("Ghiciti numarul aleatoriu: "))
#
#
# if y > x:
#     print("Numarul introdus este mai mare.")
# elif y < x:
#     print("Numarul introdus este mai mic.")
# elif x == y:
#     print("Ati ghicit!!!")