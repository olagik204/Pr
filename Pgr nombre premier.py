def est_premier(n):
    if n<= 1:
        return false
    for i in range(2, n):
        if n % i == 0:
            return false
        return true
    nombre = int(input("Entrez un nombre entier :"))
    if est_premier(nombre):
        print(f"{nombre} est un nombre premier.")
    else:
            print(f"{nombre} n'est pas un nombre premier.")
 
 
