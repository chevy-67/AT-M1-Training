def oddOrEven(*args):
    for i in args:
        if i%2==0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")

oddOrEven(1,2,3,5,4,6,1)
oddOrEven(6,2)