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