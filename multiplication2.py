# Table de multiplication par 4 
nb = int(input("Entrer un chiffre : "))

print("Table de multiplication par", nb) 
for n in range(0,11) : 
    print(n, " x ",nb ," = ",n*nb) 
print("Fin de la table de multiplication") 