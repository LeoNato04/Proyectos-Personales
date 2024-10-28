import random
index=input("¿Quieres comenzar el juego? (Si/No): ").lower()

# Inicia el juego si se responde con un "Si"
while index=="si":
    listErr=[]
    randomNumb=random.randint(1, 100)
    win=0
    i=0
    err=0
    print()
    print("Adivina mi numero, tienes 7 intentos :)")
    while win==0 and i<7:
        entry=int(input("Introduce tu numero: "))

        # Da un mensaje y no permite iniciar si el numero no esta entre 1 y 100
        if entry>100 or entry<1:
            print()
            print("Introduce un numero entre 1 y 100")
            err=1

        # Contiuna el juego si el numero introducido esta entre 1 y 100
        if entry>=1 and entry<=100:
            err=0
            
        # Termina el ciclo "for" si la respuesta es correcta          
        if entry==randomNumb and err==0:
            win=1
            print()
            print("Correcto mi numero era",randomNumb)

            # Da una respuesta si la lista de errores esta vacia
            if len(listErr)==0:
                print("No fallaste ni una vez, ¡bien hecho!")
                print()

            # Da una respuesta si la lista de errores tiene algun valor
            if len(listErr)!=0:
                print("Tus errores fueron",listErr)
                print()
                
            i=7
                
        # Contiuna el juego si el numero no es correcto
        if entry!=randomNumb and err==0:

            # Termina el juego en el ultimo intento para dar una respuesta diferente
            if i==6:
                listErr.append(entry)
                i=i+1
                
            # Contiuna el juego y da un apoyo a un numero mayor
            elif entry<randomNumb and i<7:
                msg="Fallaste tu intento "+str(i+1)
                print()
                print(msg)
                print("Mi numero es mayor a",entry)
                listErr.append(entry)
                i=i+1
                
            # Contiuna el juego y da un apoyo a un numero menor      
            elif entry>randomNumb and i<7:
                msg="Fallaste tu intento "+str(i+1)
                print()
                print(msg)
                print("Mi numero es menor a",entry)
                listErr.append(entry)
                i=i+1

    # Termina el juego y dice las respuestas del jugador            
    if i==7 and win==0:
        print()
        print("Fallaste tu ultimo intento, mi numero era",randomNumb)
        print("Tus respuestas fueron",listErr)
        print()
        
    index=input("¿Quieres continuar el juego? (Si/No): ").lower()
    
# Termina el juego si se responde con un "No"
if index=="no":
    print("¡Gracias por jugar!")
    
# Termina el programa si no se responde con "Si" o "No"        
if index!="no" and index!="si":
    print("Error: Entrada invalida")
