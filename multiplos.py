"""
Andrés Enrique Jaime de la Rosa, 763799
"""
# Entradas
na=int(input("Introduzca un número "))
nb=int(input("Introduzca otro número "))
# Proceso
multiplo = na%nb
multiplo2 = nb%na
if multiplo // 1 == 0:
    print("El número",na,"es multiplo de",nb)
elif multiplo2 // 1 == 0:
    print("El número",nb,"es multiplo de",na)
else:
    print("Ninguno de los números es múltiplo del otro")
# Salidas