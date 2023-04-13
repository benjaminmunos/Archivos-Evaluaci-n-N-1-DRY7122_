# Solicitar al usuario el número de ACL IPv4
numero_acl = input("Ingrese el número de ACL IPv4: ")

# Determinar si la ACL es Estándar del 1 al 99 o Extendida del 100 al 199
if numero_acl.isdigit():
    numero_acl = int(numero_acl)
    if 1 <= numero_acl <= 99:
        print(f"La ACL {numero_acl} es una ACL Estándar.")
    elif 100 <= numero_acl <= 199:
        print(f"La ACL {numero_acl} es una ACL Extendida.")
    else:
        print("El número de ACL IPv4 no corresponde a una lista de acceso Estándar del 1 al 99 o Extendida del 100 al 199.")
else:
    print("El número de ACL IPv4 debe ser un número entero positivo.")
