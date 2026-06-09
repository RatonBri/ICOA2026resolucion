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

## 🔍 Vulnerabilidad

El reto se basa en un **Cifrado César (Rotación de caracteres)** clásico. La solución se deduce analizando el contexto histórico y filológico de la descripción:

### 1. Contexto Histórico
El texto menciona a *Augustus* como el hijo adoptivo y heredero de un gran general (*Julio César*). En la historia de la criptografía, Julio César es mundialmente reconocido por el desarrollo del **Cifrado César**.

### 2. Análisis del Criptograma
La cadena provista conserva la estructura de mayúsculas, minúsculas y guiones bajos (`_`), lo que facilita un ataque de fuerza bruta por desplazamiento o un análisis directo de caracteres:

---

## Flag

```text
pecan{Even_Cipherz_Evolve}
