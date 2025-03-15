num_uno = 5

if num_uno == 5:
    print("El numero es cinco")

print("Fin.")


print("Sistema para calcular el promedio de un alumno.")
nom = input("Para comenzar, Cual es tu nombre?: ")

cal_uno = int(input("¿Cual es tu calificacion en Matematicas?:"))
cal_dos = int(input("¿Cual es tu calificacion en Quimica?:"))
cal_tres = int(input("¿Cual es tu calificacion en Biologia?:"))

suma = (cal_uno + cal_dos + cal_tres) / 3
suma = int(suma)


if suma >= 6:
    print("Felicidades", nom ,"aprobaste con un promedio de:", suma )

print("Fin.") 
