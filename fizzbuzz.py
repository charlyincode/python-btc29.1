nombre = 3

if nombre % 3 == 0 and nombre % 5 == 0:
    print("FizzBuzz")
elif nombre % 5 == 0:
    print("Buzz")
elif nombre % 3 == 0:
    print("Fizz")
else:
    print(nombre)