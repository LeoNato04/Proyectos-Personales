a=float(input("Introduce el valor de A:"))
b=float(input("Introduce el valor de B:"))
c=float(input("Introduce el valor de C:"))
if a==b and b==c:
    print(a,",",b,"y",c,"son iguales")
if a==c and b>c:
    print(a,"y",c,"son iguales y menores que",b)
if a==c and b<c:
    print(a,"y",c,"son iguales y mayores que",b)
if a==b and b<c:
    print(a,"es igual a",b,"que es menor que",c)
if a==b and b>c:
    print(a,"es igual a",b,"que es mayor que",c)
if a<b and b==c:
    print(a,"es menor que",b,"que es igual a",c)
if a>b and b==c:
    print(a,"es mayor que",b,"que es igual a",c)
if a<b and b<c:
    print(a,"es menor que",b,"que es menor que",c)
if a>b and b<c and a!=c:
    print(a,"es mayor que",b,"que es menor que",c)
if a>b and b>c:
    print(a,"es mayor que",b,"que es mayor que",c)
if a<b and b>c and a!=c:
    print(a,"es menor que",b,"que es mayor que",c)


