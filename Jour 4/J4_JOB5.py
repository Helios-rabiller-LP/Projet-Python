def calcule(num1:int,operator:str,num2:int):
    if operator == "+":
        return num1 + num2
    elif operator == "%":
        return num1 % num2
    elif operator == "*":
        return num1 * num2
    elif operator == "-":
        return num1 - num2
    elif operator == "/":
        return num1 / num2
    else:
        print("Erreur veuiller rentrez 2 nombres et un opérateur")
print(calcule(20,"*",4))
