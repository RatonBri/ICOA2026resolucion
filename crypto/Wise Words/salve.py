def cifradocesar(texto_cifrado):
    for desplazamiento in range(1, 26):
        resultado = []
        for caracter in texto_cifrado:
            if caracter.isalpha():
                inicio = ord('a') if caracter.islower() else ord('A')
                codigo = (ord(caracter) - inicio - desplazamiento) % 26 + inicio
                resultado.append(chr(codigo))
            else:
                resultado.append(caracter)

        print(f"Llave {desplazamiento}: {''.join(resultado)}")

mensaje = "Fwfo_Djqifsaa_Fwpmwf"
cifradocesar(mensaje)
