# Mysteries of the Tomb

## Detalles del Reto
| Atributo | Detalle |
| :--- | :--- |
| **Categoría** | Crypto / Substitution |
| **Puntos** | 100 puntos |
| **Autor** | Riley Grimwood |

---

## Descripción
> In the shadowed depths of the Valley of Kings, explorers have uncovered a tomb long lost to time. At its heart rests an ancient stone tablet, etched meticulously with mysterious glyphs—a pyramid of secrets crafted by devoted scribes guarding the pharaoh's most sacred treasure...
>
> To unveil the truth, read the stones at dawn's first light, tracing from the summit down to the shifting sands.

### Archivos del Reto
El reto nos provee dos archivos de texto que se encuentran ubicados en el directorio local:
* **[`flag.txt`](./flag.txt)**: Contiene la disposición piramidal de los jeroglíficos.
* **[`notes.txt`](./notes.txt)**: Funciona como el diccionario de traducción (alfabeto de sustitución).

---

## Vulnerabilidad

Este reto se basa en un **Cifrado de Sustitución Monoalfabética**. La dificultad real no radica en romper un algoritmo, como el RSA o OTP, sino en interpretar la lógica de lectura indicada en la descripción. En lo personal, este tipo de retos son basnate divertidos, pero demasiado frustrante, muchas veces no encontraras que tipo de simbolos te dan o una vez me tope con un ctf, en conde el autor se inspiro en una pelicula muy antigua, el cifrado se menciono solo una vez y de paso estaba en aleman, pero no niego que fue muy divertido. 

### 1. Análisis de la Pista (Dirección de Lectura)
La descripción dicta explícitamente: *"...tracing from the summit down to the shifting sands."* (Trazando desde la cumbre hacia abajo hasta las arenas movedizas).

Esto nos indica un orden de reconstrucción específico:
* **Vertical:** De arriba hacia abajo (Fila 1 a Fila 5).
* **Horizontal:** De izquierda a derecha dentro de cada nivel de la pirámide.

### 2. Extracción de Datos (`flag.txt`)
La pirámide de glifos se estructura de la siguiente manera dentro del archivo:
```text
        𓏏
       𓉔 𓏼
      ☥ 𓏺 𓆑
     𓏼 𓂋 𓅱 𓆑
    𓏽 𓈖 ☥ 𓉔
```
### 3. Sustitución de valores (`notes.txt`)

Para apoyarnos, decidi colocar esta tabla, una explcaicon visual mucho mas rápida:

## Tabla de Traducción:

| Nivel (De arriba a abajo) | Jeroglífico (De izq a der) | Carácter Traducido | Significado en Nota |
| :---: | :---: | :---: | :--- |
| **1** | `𓏏` | **T** | Shaped like bread... symbol for truth. |
| **2** | `𓉔` | **H** | Appears in royal names... |
| **2** | `𓏼` | **3** | Triple tally... |
| **3** | `☥` | **C** | The ankh... |
| **3** | `𓏺` | **1** | A single tally... |
| **3** | `𓆑` | **F** | Seemingly a viper with horns. |
| **4** | `𓏼` | **3** | Triple tally... |
| **4** | `𓂋` | **R** | Appears near temple inscriptions... |
| **4** | `𓅱` | **O** | Waterfowl... |
| **4** | `𓆑` | **F** | Seemingly a viper with horns. |
| **5** | `𓏽` | **4** | Quad marks... |
| **5** | `𓈖` | **N** | Curving like the Nile... |
| **5** | `☥` | **C** | The ankh... |
| **5** | `𓉔` | **H** | Appears in royal names... |

---

## Flag

```text
pecan{TH3C1F3ROF4NCH}
