def main():
    # Ecrivez votre code ici !
    # Attention tout votre code doit être indenté comme ce commentaire
    nombre = input("saisisez une liste de nombre séparer par des virgule")
    nombres = [int(i) for i in nombre.split(",")]
    print(nombres)
    
    for i in nombres:
        resultat = i + i
    moyenne = resultat / len(nombres)
        
    print(f"le resultat{i} est {resultat}")
    print(f"la moyenne de {moyenne}")
    
# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
    
# Demandez à l'utilisateur de saisir une liste de nombres séparés par des virgules (par exemple : 1,2,3,4), et affichez cette liste.

# Calculez et affichez la somme des nombres dans la liste.

# Calculez et affichez la moyenne des nombres dans la liste.

# Calculez et affichez le nombre de nombres dans la liste qui sont supérieurs à la moyenne.

# Calculez et affichez le nombre de nombres dans la liste qui sont pairs.