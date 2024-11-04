a = int(input("qu'elle est la longueur de cette ligne a en cm: "))
b = int(input("qu'elle est la longueur de cette ligne b en cm: "))
c = int(input("qu'elle est la longueur de cette ligne c en cm: "))
if  a == b == c:
    print("vous avez un triangle équilatéral")
elif (a*a) + (b*b) == (c*c) or (c*c) + (b*b) == (a*a) or (a*a) + (c*c) == (b*b):
    print("vous avez un triangle rectangle")
elif a == b or b == c or a == c:
    print("Vous avez un triangle isocéle") 
else:
    print("c'est un triangle ...")
