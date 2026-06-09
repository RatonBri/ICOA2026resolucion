# Incorrect Implementation of RSA

## Detalles del Reto
| Atributo | Detalle |
| :--- | :--- |
| **Categoría** | Crypto |
| **Puntos** | 100 puntos |
| **Autor** | Raahguu |

---

## Descripción
> I just learnt about Rivest-Shamir-Aldeman, and so I created my own custom implementation. Here's the message:

### Parámetros Provistos

* **Módulo ($n$):**
  ```text
    16537241065399537261146800802060451995107796665337288928060948677362154976656429797729550619497788311160926523026781503470362013597201944839389519773564618679827061417896265475971561610333659217333638238386907603525565178455941971399130722191602944445714002268747028340120907894781607422707823554701443768586256913491149809410232167277063066105859165079765281480076330718726350243973636606134346374770537701812923215229226027759112780757449828410180237267791126609342382918352166823253106960191346933601235547281
  ```
* **Exponente público ($e$):** `5`
* **Texto cifrado (`ciphertext`):**
    ```python
    [17623416832, 10510100501, 9509900499, 8587340257, 16105100000, 28153056843, 16850581551, 12166529024, 7737809375, 12762815625, 7737809375, 19254145824, 10510100501, 8587340257, 14693280768, 14693280768, 25937424601, 7737809375, 21003416576, 12166529024, 16850581551, 21924480357, 11592740743, 12166529024, 21003416576, 7737809375, 12762815625, 7737809375, 12166529024, 8587340257, 10000000000, 7737809375, 21003416576, 12166529024, 8587340257, 21003416576, 7737809375, 10000000000, 16850581551, 16105100000, 10510100501, 7737809375, 9509900499, 254803968, 19254145824, 19254145824, 345025251, 9509900499, 21003416576, 14693280768, 25937424601, 7737809375, 282475249, 282475249, 459165024, 312500000, 601692057, 30517578125]
    ```

---

## Vulnerabilidades

A pesar de utilizar un módulo $n$ masivo de 617 dígitos (equivalente a una clave robusta de 2048 bits), la seguridad del algoritmo se rompe por tres errores:

### 1. Exponente Público Demasiado Pequeño ($e = 5$)
El autor utilizó un exponente público extremadamente bajo. En la criptografía moderna, el estándar es $e = 65537$, claramente e no debe ser ese numero exacto, pero al menos si mayor a dicho número, el objetivo, nuestro mensaje cifrado debe crecer lo suficiente, para evitar que mod sea anulado, más adelante lo explico. 

### 2. Cifrado por Carácter (Ausencia de Padding)
En lugar de cifrar la flag completa como un único bloque numérico gigante, el script iteró sobre el texto y cifró cada carácter de forma individual. 
* El valor máximo de un carácter imprimible en ASCII es de apenas $m = 255$.
* Al no implementar un esquema de relleno aleatorio (*Padding* como OAEP), el mensaje resultante es extremadamente vulnerable.
* Puedo conocer la longitud de la bandera, incluso sin saber el valor de e, lograria romper el cifrado, si conociera los primeros caracteres de la flag.

### 3. El Fenómeno Matemático $m^e < n$
La fórmula estándar de RSA es:

$$c = m^e \pmod n$$

Si elevamos el carácter ASCII más alto posible ($m = 255$) a nuestro pequeño exponente ($e = 5$), el resultado es:

$$255^5 = 1,073,741,824,125 \text{ (13 dígitos)}$$

Al comparar este resultado con el módulo $n$ (617 dígitos), vemos que el dividendo es infinitamente menor que el divisor. Por lo tanto, **la operación residuo (`mod n`) no tiene ningún efecto**:

$$c = m^5 \pmod n \implies c = m^5$$

Al anularse el módulo, el cifrado RSA se degrada a una simple potencia matemática elemental. Romperlo es tan fácil como aplicar la operación inversa directa: la **raíz quinta matemática**.

$$m = \sqrt[5]{c}$$

---

## Resolución

Para explotar esta vulnerabilidad, automatizamos el cálculo de la raíz quinta exacta sobre cada elemento del array numérico y posteriormente mapeamos los enteros obtenidos a sus respectivos caracteres bajo la codificación ASCII.

### Ejemplo de Ejecución Manual (Bloque 1):
Tomemos el primer elemento del texto cifrado: `17623416832`

$$\sqrt[5]{17623416832} = 114$$

Buscando el número decimal `114` en la tabla ASCII obtenemos de forma directa el carácter: **`r`**.

---

## Script de Solución

El script automatizado encargado de procesar todos los bloques y reconstruir la cadena original se encuentra desarrollado de forma independiente en el archivo:

 **[`solve.py`](./solve.py)**

> **Nota de uso en Linux:** Para clonar localmente el entorno y ejecutar la explotación, puedes utilizar el comando nativo de la terminal:
> ```bash
> python3 solve.py
> ```

---

## Flag

```text
pecan{oh_i_really_thought_i_had_that_done_c0rr3ctly_11629}
