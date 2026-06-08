# Multi-layer

## Detalles del Reto
* **Categoría:** Crypto / Encoding
* **Puntos:** 100
* **Autor:** Karina (ECU)

## Descripción
> This thing has layers.
> `ZnJpcmEgbyBmY25wciBmcmlyYSBhdmFyIGZjbnByIGZ2ayBzIGZjbnByIGZyaXJhIHN2aXIgZmNucHIgZ2piIG1yZWIgZmNucHIgZnZrIGZyaXJhIGZjbnByIGZ2ayBzIGZjbnByIGZyaXJhIHNiaGUgZmNucHIgZ2piIG1yZWIgZmNucHIgZnJpcmEgc2JoZSBmY25wciBmdmsgcnZ0dWcgZmNucHIgZnZrIGF2YXIgZmNucHIgZnJpcmEgZ3VlcnIgZmNucHIgZnJpcmEgcQ==`

---

## Vulnerabilidad
Al observar el formato del reto y el título *"Multi-layer"*, podemos identificar que nos enfrentamos a un problema de múltiples capas de codificación y/o cifrado clásico:

1. **Capa 1 (Base64):** El texto proporcionado termina en `==`, lo cual es el clásico relleno (*padding*) de una cadena codificada en **Base64**. Los caracteres utilizados (letras mayúsculas, minúsculas y números) confirman esta sospecha.
2. **Capa 2 (Cifrado por sustitución):** Al decodificar el Base64, el resultado no revelará la flag inmediatamente de forma legible, sino un texto ofuscado. Debido a los patrones repetitivos de palabras cortas, es muy probable que se trate de un cifrado César o **ROT13**.
3. **Formato final esperado:** El resultado final debe respetar la estructura de flag solicitada para este CTF: `pecan{flag_goes_here}`.

---

## Resolución
Para resolver este reto y pelar todas las "capas", los pasos a seguir son:

1. **Decodificar Base64:** Tomar el string de la descripción y pasarlo por un decodificador Base64 para obtener el texto intermedio.
2. **Analizar/Romper el Cifrado Clásico:** Tomar el texto resultante del paso anterior y aplicarle un ataque de fuerza bruta de rotación (ROT) o sustitución alfabética hasta que aparezca texto legible en inglés o español.
3. **Extraer la Flag:** Identificar el patrón final y empaquetarlo en el formato `pecan{...}`.

---

## Script de Solución (Exploit)

---
##  The Flag:

---
## Tips 

