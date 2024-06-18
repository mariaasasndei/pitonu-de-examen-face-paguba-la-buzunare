x=float(input("Introdu val x:"))
n=int(input("Introdu puterea lui x:"))
def putere_recursiv(x,n):
    if n==0:
        return 1
    else:
        return x*putere_recursiv(x,n-1)
print(putere_recursiv(x,n))