# Multi-layer

## Detalles del Reto
| Atributo | Detalle |
| :--- | :--- |
| **Categoría** | Crypto / Encoding |
| **Puntos** | 100 puntos |
| **Autor** | Karina (ECU) |

---

## Descripción
> This thing has layers.
> `ZnJpcmEgbyBmY25wciBmcmlyYSBhdmFyIGZjbnByIGZ2ayBzIGZjbnByIGZyaXJhIHN2aXIgZmNucHIgZ2piIG1yZWIgZmNucHIgZnZrIGZyaXJhIGZjbnByIGZ2ayBzIGZjbnByIGZyaXJhIHNiaGUgZmNucHIgZ2piIG1yZWIgZmNucHIgZnJpcmEgc2JoZSBmY25wciBmdmsgcnZ0dWcgZmNucHIgZnZrIGF2YXIgZmNucHIgZnJpcmEgZ3VlcnIgZmNucHIgZnJpcmEgcQ==`

---

## Vulnerabilidad

Nuevamente el titulo nos da casi la respuesta. Nos enfrentamos a un problema de ofuscación por capas anidadas (*nested encodings*), ¿Cuantas?, no sabemos:

1. **Capa 1 (Base64):** El payload termina en el clásico `==`.
2. **Capa 2 (Cifrado César / ROT13):** Al remover el Base64, la cadena resultante sigue sin ser legible pero conserva una estructura con palabras repetitivas de 5 letras (como `fcnpr` y `frira`). Esto denota un cifrado por sustitución monoalfabética de tipo ROT13.
3. **Capa 3 (Representación Fonética de Hexadecimal):** Al aplicar ROT13, el texto resultante revela un mensaje en inglés que deletrea de forma escrita un flujo de bytes en hexadecimal (ej. la frase *"seven b"* representa el byte `7b`).
4. **Capa 4 (Hexadecimal a ASCII):** La última capa requiere interpretar los bytes hexadecimales de vuelta a su representación de caracteres legibles.

---

## Resolución

Para quitar las múltiples capas del reto directamente desde la consola de Linux, ejecutamos los siguiente comandoas, es como ingeniería inversa:

### Paso 1: Decodificación de la capa Base64:

```bash
echo "ZnJpcmEgbyBmY25wciBmcmlyYSBhdmFyIGZjbnByIGZ2ayBzIGZjbnByIGZyaXJhIHN2aXIgZmNucHIgZ2piIG1yZWIgZmNucHIgZnZrIGZyaXJhIGZjbnByIGZ2ayBzIGZjbnByIGZyaXJhIHNiaGUgZmNucHIgZ2piIG1yZWIgZmNucHIgZnJpcmEgc2JoZSBmY25wciBmdmsgcnZ0dWcgZmNucHIgZnZrIGF2YXIgZmNucHIgZnJpcmEgZ3VlcnIgZmNucHIgZnJpcmEgcQ==" | base64 -d
```

Nos da como resulatdo:
> `frira o fcnpr frira avar fcnpr fvk s fcnpr frira svir fcnpr gjb mreb fcnpr fvk frira fcnpr fvk s fcnpr frira sbhe fcnpr gjb mreb fcnpr frira sbhe fcnpr fvk rvtug fcnpr fvk avar fcnpr frira guerr fcnpr frira q`

Aqui es donde uno se pregunta, que sigue, a simple vista parecen palabras al azar, y la verdad es que si, pero hay dos opciones, si estas practicando puedes ir a [dCode](https://www.dcode.fr/identificador-cifrado), aqui podras conocer los posibles cifrados, pero si estas en la competencias, lo mas probable es que no te permitan usarlo, asi que solo queda prabar diferentes cifrados, la segunta es la experiencia, asi como reconoces Base64, tambien reconoceras poco a poco los cifrados, o al menos podras reducir la lista, es mas que todo práctica.


### Paso 2: Cifrado César:

Okey, probemos Cesar, pero cual es nuetra llave numerica, o el desplazamiento, bueno, utilicemos un pequeño codigo que nos para todas las combinaciones posibles.

```bash
echo "ZnJpcmEgbyBmY25wciBmcmlyYSBhdmFyIGZjbnByIGZ2ayBzIGZjbnByIGZyaXJhIHN2aXIgZmNucHIgZ2piIG1yZWIgZmNucHIgZnZrIGZyaXJhIGZjbnByIGZ2ayBzIGZjbnByIGZyaXJhIHNiaGUgZmNucHIgZ2piIG1yZWIgZmNucHIgZnJpcmEgc2JoZSBmY25wciBmdmsgcnZ0dWcgZmNucHIgZnZrIGF2YXIgZmNucHIgZnJpcmEgZ3VlcnIgZmNucHIgZnJpcmEgcQ==" | base64 -d
```

Nos da como resulatdo:
> `seven b space seven nine space six f space seven five space two zero space six seven space six f space seven four space two zero space seven four space six eight space six nine space seven three space seven d`
---

## Tips

