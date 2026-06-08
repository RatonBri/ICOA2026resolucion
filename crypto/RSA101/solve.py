
n = 914224879713534891752745051672415462330144197757968187295993
e = 17
c = 152293808340616594229073242267037730353433147091103189533666

# Estos son los factores primos, puedes usar python para hallarlo, solo te adviert que tardara mucho y es basnate pesado, pero intentalo
p = 929950943285269166162048432303
q = 983089362202076727325366678231


# Cálcular función Toquiente de Euler (phi)
phi = (p - 1) * (q - 1)

# Python permite calcular inversos modulares haciendo pow(base, -1, modulo)
d = pow(e, -1, phi)

# Descifrado del criptograma (m = c^d mod n)
m = pow(c, d, n)

# Convertir a ASCII
mensaje_hex = hex(m)[2:]

# Si la longitud es impar, le agregamos un cero al inicio para que el parseo sea correcto
if len(mensaje_hex) % 2 != 0:
    mensaje_hex = '0' + mensaje_hex

# Traducimos los bytes de Hexadecimal a string legible
flag = bytes.fromhex(mensaje_hex).decode('utf-8')

print(f"Flag: {flag}")
