def time_to_text(a:int):
    if type(a) != int :
         print(str(a)+" n'est pas un nombre entier")
    elif a < 0:
        print("c'est un  nombre entier négatif") 
    else:
        hour = a // 60
        minutes = a % 60
        print(str(hour)+" heures et "+ str(minutes) + " minutes")
time_to_text("AODK")
