for i in range(1,1001):
    if i== 2 or i== 3 or i == 5 or i == 7 or i ==11 or i==13 or i==17 or i==19 or i==23 or i==29 or i==31:
        print(i)
    elif i%2==0 or i%3==0 or i%5==0 or i%7==0 or i%11==0 or i%13==0 or i%17==0 or i%19==0 or i%23==0 or i%29==0 or i%31==0 or i==1:
        continue
    else:
        print(i)
    
