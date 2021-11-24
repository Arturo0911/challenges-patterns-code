
''' Calcular A=√B^n'''

def calculo(b,n):
    if n==0:
        return (1)
    else:
        return(b*calculo(b,((n**0.5)-1)))
        
    

print(calculo(7,4))
