

# 2 ^ b

# hasta que tengamos b veces la multiplicacion
# 2 * 2 ** 2 ** ............2 ** 1
def exponente(numero):
    if numero == 0: # O(1) => 1
        return 1 # O(1) => 1  y juntos suman 2
    else:
        return 2 * exponente(numero-1)

"""
    { 2;        caso base es cuando n(o sea exponente) es igual a 0}
    { 2 + Ts(n-1);          caso general cuando n(o sea exponente) es diferente de 0}
"""


if __name__ == "__main__":

    print(exponente(5))