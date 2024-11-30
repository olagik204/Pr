def fact(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
        return resultat
    nombre = int(input("Entrez un npmbre entier :"))
    if nombre < 0:
        print("La factorielle n'est pas définie pour les nombres négatifs.")
    else:
        print(f"La factorielle de {nombre} est : {factorielle(nombre)}")
   
