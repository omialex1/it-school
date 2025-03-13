# 42) Sa se creeze un tuple cu 5 elemente diferite
# si sa se afiseze al doilea si ultimul element.
# 43) Sa se creeze 2 tuple cu cate 3 elemente fiecare.
# Sa se concateneze cele doua si sa se afiseze noul tuple rezultat in urma operatiei.
# 44) Sa se creeze un tuplu cu 10 elemente.
# Sa se citeasca de la tastatura un element si sa se verifice daca elementul se afla in tuplul creat.
# 45) Sa se creeze un tuple cu 5 elemente.
# Sa se citeasca un element de la tastatura si sa se afiseze indexul elementului in acel tuple.
# In caz ca nu se regaseste in tuple, sa se afiseze "not found".
# 46) Sa se creeze un tuplu cu 10 elemente.
# Sa se extraga un subtuplu din el pornind de la pozitia 2 pana la pozitia 5 si sa se afiseze.
# 47) Se da o lista [1,1,2,2,2,3,4,5,5,5,5,6,7,8,9,9,9].
# Sa se stearga elementele duplicate si sa se afiseze rezultatul.
# 48)Se dau doua seturi: {1,2,3,4,5,6} si {4,5,6,7,8,9}.
# Sa se afiseze elementele care se afla in ambele seturi.



# 42) Sa se creeze un tuple cu 5 elemente diferite
# si sa se afiseze al doilea si ultimul element.

# tup = (1,2,3,4,5)
# print(tup)
# print(tup[1],tup[-1])



# 43) Sa se creeze 2 tuple cu cate 3 elemente fiecare.
# Sa se concateneze cele doua si sa se afiseze noul tuple rezultat in urma operatiei.


# tup1 = (1,2,3)
# tup2 = (4,5,6)
# tup3 = tup1 + tup2
# print(tup3)



# 44) Sa se creeze un tuplu cu 10 elemente.
# Sa se citeasca de la tastatura un element si
# sa se verifice daca elementul se afla in tuplul creat.

# tup = (1,2,3,4,5,6,7,8,9,10)
# numar = int(input("Indrodu un numar si vezi daca se afla in tuplu: "))
# gasit = False
#
# for el in tup:
#     if el == numar:
#         print(numar)
#         gasit = True
#         break
# if not gasit:
#     print(f"{numar} NU se regaseste in tuplu.")



# 45) Sa se creeze un tuple cu 5 elemente.
# Sa se citeasca un element de la tastatura si sa se afiseze indexul elementului in acel tuple.




# tup = ("Eu", "Tu", "El", "Ea", "Noi")
# pronume = input("Introdu un pronume personal: ")
# pronume = pronume.lower()
# flag = False
#
# for el in tup:
#     if el.lower() == pronume:
#         print(tup.index(el))
#         flag = True
#         break
#
# if not flag:
#     print("Incearca alt pronume personal!")



# 46) Sa se creeze un tuplu cu 10 elemente.
# Sa se extraga un subtuplu din el pornind de la pozitia 2 pana la pozitia 5 si sa se afiseze.

# tup = (1,2,3,4,5,6,7,8,9,10)
#
# tup2 = tup[2:6]
# print(tup2)



# 47) Se da o lista [1,1,2,2,2,3,4,5,5,5,5,6,7,8,9,9,9].
# Sa se stearga elementele duplicate si sa se afiseze rezultatul.


# lista = [1,1,2,2,2,3,4,5,5,5,5,6,7,8,9,9,9]
# lista2 = []
# for el in lista:
#     if el not in lista2:
#         lista2.append(el)
# print(lista2)



# 48)Se dau doua seturi: {1,2,3,4,5,6} si {4,5,6,7,8,9}.
# Sa se afiseze elementele care se afla in ambele seturi.

# set1 = {1,2,3,4,5,6}
# set2 = {4,5,6,7,8,9}
#
# for el in set1 and set2:
#     if el in set1 and el in set2:
#         print(el)



# 49) Sa se scrie un program care tine evidenta elevilor dintr-o scoala.
# Programul trebuie sa dispuna de un meniu care ne pune la dispozitie urmatoarele optiuni:
#
# 1.Adaugare elev
# 2.Afisarea elevilor existenti
# 3.Modificare informatii elev existent
# 4.Stergere elev
# 5.Cautare elev dupa nume si prenume
# 6.Afisare elevi in ordinea mediei
# 7.Afisare elevi cu media peste 8
# 8.Afisare elevi in ordine alfabetica (in functie de Nume)
# 9.Iesire din program
#
# Pentru fiecare elev trebuie sa retinem urmatoarele informatii:
# Nume
# Prenume
# Nota romana
# Nota matematica
# Nota engleza
# Media (sa se calculeze automat pe baza notelor introduse)











