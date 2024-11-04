try:
    age = (int(input("Quel est votre âge ? :")))
    if age == 17:
        print("Vous êtres presque majeur")
    elif 12 <= age < 18:
        print("Vous êtes adolescent")
    elif age == 1 or age == 2:
        print("Vous êtes un bébé")
    elif age >= 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur") 
except:
    print("Erreur vous devez rentrez un nombre pour votre âge !")