personne = {
    "nom" : "Wandja",
    "prenom" : "Charly"
}

prenom = personne["prenom"]
print(prenom)
keys = personne.keys()
print(keys)
values = personne.values()
print(values)
print(personne.items())

personne['age'] = 35
print(personne)
personne['age'] = 5
print(personne)

personne.pop("age")
print(personne)

if "nom" in personne:
    print("il y a bien un nom")

if "age" not in personne:
    print("il n'y a pas d'age")