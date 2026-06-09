def Cifradocesar (texto_cifrado):
    # Probamos todos los desplazamientos posibles (del 1 al 25) por las letras del alfabeto, no contamos ñ
    for desplazamiento in range(1, 26):
        resultado = []
        for caracter in texto_cifrado:
            if caracter.isalpha():
                # Obtenemos el código ASCII y definimos el inicio del alfabeto
                inicio = ord('a') if caracter.islower() else ord('A')
                # Aplicamos la fórmula
                codigo = (ord(caracter) - inicio - desplazamiento) % 26 + inicio
                resultado.append(chr(codigo))
            else:
                # Mantenemos los espacios y signos de puntuación intactos
                resultado.append(caracter)

        print(f"Llave {desplazamiento}: {''.join(resultado)}")


mensaje = "frira o fcnpr frira avar fcnpr fvk s fcnpr frira svir fcnpr gjb mreb fcnpr fvk frira fcnpr fvk s fcnpr frira sbhe fcnpr gjb mreb fcnpr frira sbhe fcnpr fvk rvtug fcnpr fvk avar fcnpr frira guerr fcnpr frira q"
Cifradocesar(mensaje)
