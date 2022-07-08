def pattern(NUM2):
    for i in range (0,NUM2):
        for j in range(0,i+1):
            print(j,end ="")
        print("\r")
NUM2=int(input("Enter the number = "))
pattern(NUM2)
