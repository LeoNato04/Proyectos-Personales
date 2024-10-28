import math
a=float(input("Introduzca el valor de lado A:"))
b=float(input("Introduzca el valor del lado B:"))
ang=float(input("Introduzca el valor del angulo:"))
radi=(ang*math.pi)/180
c=math.sqrt((b**2)+(a**2)-(2*b*a)*(math.cos(radi)))
p=a+b+c
s=p/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("El area del triangulo es:", area)
