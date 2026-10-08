def helloWorld():
    print("Hello World")

helloWorld()
helloWorld()
helloWorld()

def bonjour(prenom):
    print(f"Bonjour {prenom}")

bonjour("Charly")
bonjour("toi")

def hello(prenom, nom):
    print(f"Hello {prenom} {nom}")

hello("Charly","Wandja")

def mot(m = "Python"):
    print(m)

mot("toto")
mot()

def triple(num):
    return 3 * num

res = triple(6)
print(res)

def inverse(x):
    if(x==0):
        return "impossiblle de faire 1/0"
    return 1 /x

print(inverse(0))
print(inverse(2))

def factoriel(n):
    if n==0:
        return 1
    return n * factoriel(n-1)

print(factoriel(3))