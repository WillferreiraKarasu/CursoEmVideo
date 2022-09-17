def soma(a,b):
    s = a + b
    print(s)

soma(5,3)
soma(2,1)
soma(3,4)

def contador(*num):
    for c in num:
        print(f'{c} ', end=' ')


contador(2,1,7)
contador(8,2)
contador(1,2,3,4,5,6)