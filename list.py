fruits = ["pomme", "banane", "orange", "mangue"]
nombre = [1, 2, 3, 4, 5, 6, 7]
mixte = [1, "deux", True, 3.14]
vide = []

longueur = len(fruits)
print(longueur)

#acces
first = fruits[0]
print(first)
banane = fruits[1]
print(banane)
last = fruits[-1]
print(last)
print(nombre[1:4])
print(nombre[:5])
print(nombre[3:])
print(nombre[-4:-1])

#change
fruits[0] = "poire"
print(fruits)
fruits[1:3] = ["melon","pasteque"]
print(fruits)
fruits[1:2] = ["fraise","framboise"]
print(fruits)
fruits[1:3]= ["raisin"]
print(fruits)

#insert
fruits.append("ananas")
print(fruits)
fruits.insert(1,"kiwi")
print(fruits)
fruits.extend(["peche","abricot"])
print(fruits)

#supprimer
fruits.remove("abricot")
print(fruits)
fruits.pop(1)
print(fruits)

#trier
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

fruits2 = fruits
print(fruits)
print(fruits2)
fruits[0]= "cerise"
print(fruits)
print(fruits2)
fruits2 = fruits.copy()
fruits[0]= "fraise"
print(fruits)
print(fruits2)

matrice =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrice[1][0])

if "poire" in fruits:
    print("Trouvé !")

if "pomme" not in fruits:
    print("il n'y a bien aucune pomme")