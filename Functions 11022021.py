def funcA():
    x = 8 #value (local var)
    print(x) #print value (local var)

def funcB():
    print(sqr(x)) #print sqrt of value (global var)
    print(sqrt(x))

def sqr(i):
    return i * i

def sqrt(i):
    x = 1
    while x > 0:
        if x * x == i:
            break
        else:
            x += 1
    return(x)
        
x = 256
funcA()
funcB()


print('justin')
