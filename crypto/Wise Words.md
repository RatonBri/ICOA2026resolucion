# Wise Words

---

## Ficha Técnica

| Parámetro | Detalle |
| :--- | :--- |
| **🏷️ Categoría** | `Crypto` / `Criptografía Clásica` |
| **✨ Puntos** | 260 PTS |
| **👤 Autor** | [@Riley Grimwood](https://github.com) |

---

## Descripción del Reto

> **Enunciado Original:**
> _"I once encountered Augustus, the adopted son and heir of a great general. When I asked him what his greatest strategy was, he simply whispered: Fwfo_Djqifsaa_Fwpmwf"_

### 🔑 Pista Clave Detectada
El texto hace referencia directa a **Augustus** (César Augusto), el hijo adoptivo y heredero de Julio César. En el contexto de la criptografía, esto es una referencia histórica directa al **Cifrado César**.

---

## 🔍 Análisis de Vulnerabilidades

Al investigar el contexto histórico de los métodos de comunicación de Augusto, encontramos el siguiente vector de ataque:

### 🚨 1. Cifrado César Modificado (Shift de Augusto)
A diferencia de Julio César (que utilizaba históricamente un desplazamiento de 3 posiciones en el alfabeto), los historiadores como Suetonio documentaron que **Augusto utilizaba un desplazamiento de exactamente 1 posición ($k = 1$)** hacia la derecha, y no rotaba al principio del alfabeto, sino que escribía `AA` si necesitaba una `Z`.

### 🚨 2. Análisis del Ciphertext
Si tomamos la cadena `Fwfo_Djqifsaa_Fwpmwf` y desplazamos cada letra una posición hacia atrás en el abecedario ($k = -1$):
* `F` $\rightarrow$ `E`
* `w` $\rightarrow$ `v`
* `f` $\rightarrow$ `e`
* `o` $\rightarrow$ `n`

> [!TIP]
> La primera palabra se traduce claramente como **"Even"**, lo que valida al 100% que la vulnerabilidad del mensaje es un cifrado de sustitución monoalfabética por rotación de un solo carácter.

---

## 🛠️ Estrategia de Resolución (Plan de Ataque)

```mermaid
graph TD
    A[Leer Ciphertext] --> B(Identificar Caracteres Especiales '_')
    B --> C[Aplicar Rotación César K = -1]
    C --> D[Ignorar Guiones Bajos en la Rotación]
    D --> E[🎉 Construir Flag con Formato pecan]
