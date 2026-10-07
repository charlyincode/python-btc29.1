articles =[
    {
        "titre" : "Titre 1",
        "contenu": "contenu 1"
    },
    {
        "titre" : "Titre 2",
        "contenu": "contenu 2"
    },
    {
        "titre" : "titre 3",
        "contenu" : "contenu 3"
    }
]

#for article in articles:
#    print("le titre:",article["titre"])
#    print("l'article:",article["contenu"])
#    print("-----------")

for i in range(len(articles)):
    print("le titre:",articles[i]["titre"])
    print("l'article:",articles[i]["contenu"])
    if i != len(articles) -1:
        print("-----------")