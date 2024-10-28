cons=True
con=input("¿Quieres comenzar el juego?")
con=con.lower()

if con=="si":
    con=True
elif con=="no":
    con=False
    
while con==True and cons==True:
    import math
    import random
    
    n=int(input("Introduce un numero: "))
    x=random.randint(0, n)
    y=random.randint(0, n)
    rs="¿Cuál es la multiplicación entre "+str(x)+" y "+str(y)+"? "
    r=int(input(rs))
    if r==x*y:
        print("Correcto, el resultado es igual a:",x*y)
    elif r!=x*y:
        print("Incorrecto, su multiplicación es:",x*y)
        
    cons=input("¿Deseas continuar jugando?")
    if cons=="si":
        cons=True
    elif cons=="no":
        cons=False

if con==False or cons==False:
    print("Programa terminado, gracias por participar!")
