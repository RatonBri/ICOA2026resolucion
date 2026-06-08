#Este codigo est para sagemath

from sage.all import *

n = 914224879713534891752745051672415462330144197757968187295993
e = 17
c = 152293808340616594229073242267037730353433147091103189533666


# Factorizar n
factores = factor(n)
lista_factores = list(factores)

p = lista_factores[0][0]
q = lista_factores[1][0]

print(f"[+] Factor p encontrado: {p}")
print(f"[+] Factor q encontrado: {q}")

# Cálcular la función Toquiente de Euler
phi = (p - 1) * (q - 1)

# Cálcular la clave privada 'd' (Inverso multiplicativo modular)
d = inverse_mod(e, phi)

# Descifrar el criptograma (m = c^d mod n)
m = power_mod(c, d, n)

# Convertimos el entero de Sage a un entero estándar de Python para poder usar hex()
mensaje_hex = hex(int(m))[2:]

# Aseguramos que la cadena hex tenga una longitud par
if len(mensaje_hex) % 2 != 0:
    mensaje_hex = '0' + mensaje_hex

flag = bytes.fromhex(mensaje_hex).decode('utf-8')

print(f"Flag: {flag}")
