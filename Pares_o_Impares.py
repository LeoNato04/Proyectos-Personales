p=input("Pares o Impares:")
p=p.lower()
n=int(input("Introduce el numero:"))
xp=2
xi=1
if p=="par" or p=="pares":
    while xp<n:
            print(xp)
            xp=xp+2
    if xp==n:
        print(xp)
        print("END")
    elif xp>n:
        print("END")
if p=="impar" or p=="impares":
    while xi<n:
            print(xi)
            xi=xi+2
    if xi==n:
        print(xi)
        print("END")
    elif xi>n:
        print("END")


