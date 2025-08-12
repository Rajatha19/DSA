def armstrong(n):
    digits=str(n)
    power=len(digits)
    total=sum(int(d)**power for d in digits)
    return total==n
n=int(input())
print(armstrong(n))
