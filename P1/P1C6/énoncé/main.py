#Créez une liste nommée  fruits  contenant les éléments  pomme  ,  banane  et  orange  .
fruits = ["pomme","banane","orange"]
#Ajoutez  kiwi  à la liste  fruits  .
fruits.append("kiwi")
print(fruits)

#Supprimez  orange  de la liste  fruits  .
fruits.remove("orange")
print(fruits)

#Modifiez le deuxième élément de la liste  fruits  en  ananas  .
fruits[1] = "ananas"
print(fruits)

#Affichez la longueur de la liste  fruits  .
print(len(fruits))

#Triez la liste  fruits  par ordre alphabétique et affichez-la.
fruits.sort() 
print(fruits)