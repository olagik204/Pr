def calculer_pgcd(a, b):
     for i in range(min(a, b), 0,-1):
         if a% i ==0 and b % i== 0:
             return i
nombre1 = int(input("Entrez le premier nombre entier : "))
nombre2 = int(input("Entrez le deuxième nombre entier : "))
print(f"Le PGCD de {nombre1} et {nombre2} est: {calculer_pgcd(nombre1,nombre2)}")
