fruits = {"pomme", "banane", "orange", "mangue", "pomme"}
print(fruits)
fruits.add("poire")
print(fruits)
fruits.update({"melon", "pasteque"})
print(fruits)
fruits.remove("banane")
print(fruits)
# fruits.remove("figue") #provoque une erreur
fruits.discard("orange")
print(fruits)
fruits.discard("figue")