jour = "h"

match jour:
    case 1:
        print("Lundi")
    case 2:
        print("Mardi")
    case 3:
        print("Mercredi")
    case 4:
        print("Jeudi")
    case 5:
        print("Vendredi")
    case 6:
        print("Samedi")
    case 7:
        print("Dimanche")
    case _:
        print("Erreur")

match jour:
    case 1 | 2 |3 | 4 | 5 :
        print("C'est la semaine")
    case 6 | 7:
        print("C'est le week-end")