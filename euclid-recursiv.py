a=int(input("introdu valoare pt a:"))
b=int(input("introdu valoare pt b:"))
def cmmdc(a,b):
    if b==0:
        return a
    else:
        return cmmdc(b,a%b)
print (cmmdc(a,b))
