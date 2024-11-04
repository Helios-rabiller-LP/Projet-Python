def pair(a):
    if not a == int:
         print(str(a)+" n'est pas un nombre entier")
    elif a < 0:
        print("c'est un  nombre entier négatif") 
    else:
        if a % 2 ==0:
            print(str(a)+" est pair !")
        else:
            print(str(a)+" est impair !")
       
pair("ABCDSER")