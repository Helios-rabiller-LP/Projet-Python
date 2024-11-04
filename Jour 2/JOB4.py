N = int(input("Entrer un entier supérieur a 0 : "))
i = 0




while i <= N :
    print("Table de multiplication de", i)
    for e in range(1,11):
        print(i, "x", e, "=", int(i*e))
    i = i + 1
    print(" ")
