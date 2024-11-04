nom = "Voitures"
prix_unit = 50000
qt_stock = 100

print("Bienvenue nous disposons de "+(str(qt_stock))+" "+(nom)+" en stock pour un prix a l'unité de "+(str(prix_unit))+" euro." )
achat = input("Combien de "+ nom+" voulez vous achetez ?")
qt_stock = (qt_stock-int(achat))
prix_achat = (prix_unit*int(achat))
print ("Merci pour votre achat de "+ (str(achat)) +" "+ nom +" au prix total de "+ (str(prix_achat)))
print ("Le nouveau stock de "+ nom + " est de "+ (str(qt_stock)))
prix_unit = prix_unit*1.1
print("Nous disposons de "+(str(qt_stock))+" "+(nom)+" en stock pour un prix a l'unité de "+(str(round(prix_unit)))+" euro." )
