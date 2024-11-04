def Tapis(n):
    
    print("+" + "-" *(n+1) + "+")
    for i in range(n):
        print("|"+"#"*i+" "*(n-i) + "#"+"|")
    print("+" + "-" *(n+1) + "+")
Tapis(20)


