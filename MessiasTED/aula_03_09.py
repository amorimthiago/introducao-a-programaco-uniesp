
a = 2
b = 7
c = 3.5
L = False

A = ( b == a * c and L) # a
B = (b > a or b == a^a ) # b
C = (L and b % a >= c or not a <= c) # c
D = ( b/a == c or b/a != c) # d


print("O resultado das alternativas:")

print("Letra A =", A)
print("Letra B =", B)
print("Letra C =", C)
print("Letra D =", D)
