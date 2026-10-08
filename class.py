class Article:
    def __init__(self, titre, contenu):
        self.titre = titre
        self.contenu = contenu

    def details(self):
        print("Le titre :",self.titre)
        print("Le contenu :", self.contenu)

article = Article("titre 1","contenu 1")
print(article.titre)
print(article.contenu)

article.details()

class User:
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom

    def hello(self):
        print(f"Bonjour je m'appelle {self.prenom} {self.nom}")

p1 = User("Doe","John")
p2 = User("Doe","Jane")
print(p1.nom, p1.prenom)
print(p2.nom, p2.prenom)
p1.hello()
p2.hello()

