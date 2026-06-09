# Writeup: Wise Words

## Detalles del Reto
| Atributo | Detalle |
| :--- | :--- |
| **Categoría** | Crypto / Substitution |
| **Puntos** | 260 puntos |
| **Autor** | Riley Grimwood |

---

## Descripción
> I once encountered Augustus, the adopted son and heir of a great general. When I asked him what his greatest strategy was, he simply whispered: `Fwfo_Djqifsaa_Fwpmwf`

---

## Vulnerabilidad

El reto se basa en un **Cifrado César (Rotación de caracteres)** clásico. La solución se deduce analizando el contexto histórico y filológico de la descripción:

### 1. Contexto Histórico
El texto menciona a *Augustus* como el hijo adoptivo y heredero de un gran general (*Julio César*). En la historia de la criptografía, Julio César es mundialmente reconocido por el desarrollo del **Cifrado César**.

Okey aqui hay algo curioso, primero usamos nuestro codigo de cifrado Cesar [`solve.py`](./solve.py).

Ya hecho eso, vemos que nos da:

```text
    Even_Cipherzz_Evolve
```

Y aqui creo que es la parte donde te cuestionas, ¿Por que decidiste dedicarte a esto?, okey es una exageracion mia, pero realmente fue un dolor de cabeza encontrar el error. Me paso por la mente dejarte el reto a ti, pero bueno. Por eso siempre recuerda el formato y de paso, una que otra combinacion.

---

## Flag

```text
pecan{Even_Cipherz_Evolve}
