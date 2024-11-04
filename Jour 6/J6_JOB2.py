def triangle(height):
    height=height-1
    for i in range(height):
        print(" "* (height-i)+"/" + " " *(i *2) +"\ ")
    print("/"+"_"*(height*2)+"\ ")

for i in range(0,20):
    print(triangle(i))
