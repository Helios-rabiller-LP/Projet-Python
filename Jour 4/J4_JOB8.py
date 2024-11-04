def saisonnier(type,saison):
    if type == "fruit" and saison == "hiver":
        print("orange,mandarine,kiwi")
    elif type == "fruit" and saison == "été":
        print("poire,fraise,cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte,topinambour,endive")
    elif type == "legume" and saison == "été":
        print("artichaut,aubergine,navet")
    else:
        print("je ne connais pas ce type ni ce fruit")
saisonnier("fruit","hiver")
