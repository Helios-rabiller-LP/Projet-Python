def Tapis(n):
    
    print("+" + "-" *(n+1) + "+")
    for i in range(n):
        print("|"+"#"*(n-i)+" "+ "#"*i+"|")
    print("+" + "-" *(n+1) + "+")
Tapis(100)


