n=int(input("Introdu nr:"))
def Fibo_Rec(n,memo={ }):
    if n in memo:
        return memo[n]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        memo[n]= Fibo_Rec(n-1,memo)+Fibo_Rec(n-2,memo)
        return memo[n]
print (Fibo_Rec(n))
