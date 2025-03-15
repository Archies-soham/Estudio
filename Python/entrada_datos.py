palabra = input("Introduce una palabra: ")
num_int = int(input("Introduce un numero entero: "))
num_float = float(input("Introduce un numero flotante: "))
num_compl = complex(input("Introduce un numero complejo: "))

print("String:",palabra)
print("Entero:",num_int)
print("Flotante:",num_float)
print("Numero complejo:",num_compl)


#Al usar la palabra reservada input el programa solo recibira texto (String), antes de introducir datos es necesario que se le diga al sistema que dato va a recibir en muchos casos (int, float , complex etc...)