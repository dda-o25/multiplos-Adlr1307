"""
Andrés Enrique Jaime de la Rosa, 763799
"""
# Entradas
na=int(input("Introduzca un número "))
nb=int(input("Introduzca otro número "))
# Proceso
if na == 0 and nb == 0:
    print("Los dos números no pueden ser 0")
elif na == 0:
    print("El número",na,"es múltiplo del",nb)
elif nb == 0:
    print("El número",nb,"es múltiplo del",na)
else:    
    multiplo = na%nb
    multiplo2 = nb%na
    if multiplo == 0:
        print("El número",na,"es múltiplo del",nb)
    elif multiplo2 == 0:
        print("El número",nb,"es múltiplo del",na)
    else:
        print("Ninguno de los números es múltiplo del otro")



# Salidas