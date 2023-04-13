print("Evaluación N°1 Programación y Redes Virtualizadas")
integrantes = []
while True:
    nombre = input("Ingrese el nombre del integrante, para terminar escriba 'fin': ")
    if nombre == 'fin':
        break
    else:
        integrantes.append(nombre)

print("Los integrantes de la evaluación son:")
for integrante in integrantes:
    print("- " + integrante)
