#  TEMA 3

# 33. Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel], [10.2, 7.5, 3.4]].
# Sa se extraga numele "Ionut" din lista si sa se afiseze.

# lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]
#
# nume = lista[1][1]
# print(nume)


#34. Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel], [10.2, 7.5, 3.4]].
# Sa se extraga litera "r" din numele "Marcel" si sa se afiseze.

# lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]
#
# litera_r = lista[1][2][2]
# print(litera_r)


# 35. Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]].
# Sa se afiseze toate numerele de tip float din lista.

# lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]
#
# for element in lista:
#     for element_float in element:
#         if type(element_float) == float:
#             print(element_float)


# 36. Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]].
# Scrieti un program care citeste un nume de la tastatura si verifica daca numele se afla in lista.


# nume = input("Introduceti un prenume cu majuscula: ")
#
# lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]
#
# for element in lista:
#     for element_nume in element:
#         if element_nume == nume:
#             print(f"Numele '{nume}' exista in lista.")


# 37. Se da lista: [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97].
# Sa se afiseze numerele pare din lista.


# lista = [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]
#
# for element in lista:
#     if element % 2 == 0:
#         print(element)


# 38. Se da lista: [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97].
# Sa se afiseze cel mai mic numar si cel mai mare numar din lista.

# lista = [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]
# cel_mai_mare= max(lista)
# cel_mai_mic = min(lista)
# print(cel_mai_mare)
# print(cel_mai_mic)


#39. Sa se scrie o functie care primeste ca parametru lista si un numar.
# Functia trebuie sa afiseze toate numerele din lista care sunt divizibile cu numarul dat.
# Numarul dat este introdus de la tastatura de catre utilizatorul programului.


# lista = [1, 2, 3, 5, 4, 6]
# numar = int(input("Introduceti un numar: "))
#
#
# def functie(lista, numar):
#     for el in lista:
#         if el % numar == 0:
#             print(el)
#
#
# functie(lista, numar)



# 40. Se da lista: [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97].
# Sa se scrie o functie care primeste ca parametru lista si afiseaza suma numerelor impare din lista.


# lista = [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]
# lista_2 = []
# def functie(lista):
#     for el in lista:
#         if el % 2 == 1:
#            lista_2.append(el)
#
#
#     print(sum(lista_2))
#
# functie(lista)



# 41. Se da lista: [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97].
# Sa se scrie o functie care primeste ca parametru lista si un numar.
# Functia trebuie sa afiseaza indexul numarului daca
# acesta se afla in lista sau "Not Found" in caz contrar.


# lista = [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]
# numar = int(input("Introduceti un numar: "))
#
# def functie(lista, numar):
#     for el in lista:
#
#        if el == numar:
#            print(lista.index(el))
#            break
#     else:
#         print("Not found")






functie(lista,numar)
