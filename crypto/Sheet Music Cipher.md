# 🏆 CTF Writeup: Sheet Music Cipher

---

## 📊 Ficha Técnica

| Parámetro | Detalle |
| :--- | :--- |
| **🏷️ Categoría** | `Crypto` / `Steganography` |
| **✨ Puntos** | 336 PTS |
| **👤 Autor** | [@Raahguu](https://github.com) |
| **❤️ Feedback** | 👍 1 (25% liked) |

---

## 📜 Descripción del Reto

> 💡 **Enunciado Original:**
> _"No one will ever know that I used a Compound Motivic Musical Cipher. I can merely play music out loud and send messages without anyone being any the wiser."_

### 🔑 Pista Clave Detectada
El autor menciona explícitamente un **Compound Motivic Musical Cipher**. Esto implica que el mensaje secreto fue transformado en una pieza musical o una secuencia de notas estándar donde los tonos, acordes o motivos melódicos representan caracteres alfabéticos.

---

## 🔍 Análisis de Vulnerabilidades

Al auditar la lógica detrás de los cifrados musicales, identificamos los siguientes vectores de análisis:

### 🚨 1. Cifrado Musical Estándar (Esteganografía Acústica)
Históricamente (como el sistema de Michael Haydn o el de Johann Sebastian Bach), los cifrados musicales asignan letras a las notas de la escala musical (`A, B, C, D, E, F, G` en la notación anglosajona, correspondientes a `La, Si, Do, Re, Mi, Fa, Sol`). 

### 🚨 2. El Factor "Compuesto" y "Motívico"
Al llamarse *"Compound Motivic"*, el reto no solo utiliza notas individuales individuales, sino que probablemente agrupa las notas en **motivos** (bloques de compases o patrones de ritmo) que se repiten para representar letras más complejas o palabras enteras, rompiendo la sustitución simple.

> [!NOTE]
> Dependiendo de los archivos adjuntos del reto (un archivo de audio `.wav`/`.mp3`, un archivo `.midi`, o una imagen de una partitura `.png`), el ataque consiste en extraer la secuencia exacta de notas musicales interpretadas.

---

## 🛠️ Estrategia de Resolución (Plan de Ataque)

```mermaid
graph TD
    A[Analizar Archivo Musical / Partitura] --> B[Extraer Secuencia de Notas MIDI / Tonos]
    B --> C{¿Sustitución Simple o Compuesta?}
    C -- Notas a Letras --> D[Mapear Frecuencias al Alfabeto]
    C -- Patrones Rítmicos --> E[Descifrar Motivos Repetitivos]
    D --> F[🎉 Reconstruir Flag pecan]
    E --> F
