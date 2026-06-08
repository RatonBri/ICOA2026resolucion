# Incorrect Implementation of RSA

## Detalles del Reto
* **Categoría:** Crypto
* **Puntos:** 100
* **Autor:** Raahguu

## Descripción
> I just learnt about Rivest-Shamir-Aldeman, and so I created my own custom implementation. Here's the message:

### Informacion:
* **Modulo ($n$):** `16537241065399537261146800802060451995107796665337288928060948677362154976656429797729550619497788311160926523026781503470362013597201944839389519773564618679827061417896265475971561610333659217333638238386907603525565178455941971399130722191602944445714002268747028340120907894781607422707823554701443768586256913491149809410232167277063066105859165079765281480076330718726350243973636606134346374770537701812923215229226027759112780757449828410180237267791126609342382918352166823253106960191346933601235547281`
* **Exponente público ($e$):** `5`
* **Texto cifrado (ciphertext):** `[17623416832, 10510100501, 9509900499, 8587340257, 16105100000, 28153056843, 16850581551, 12166529024, 7737809375, 12762815625, 7737809375, 19254145824, 10510100501, 8587340257, 14693280768, 14693280768, 25937424601, 7737809375, 21003416576, 12166529024, 16850581551, 21924480357, 11592740743, 12166529024, 21003416576, 7737809375, 12762815625, 7737809375, 12166529024, 8587340257, 10000000000, 7737809375, 21003416576, 12166529024, 8587340257, 21003416576, 7737809375, 10000000000, 16850581551, 16105100000, 10510100501, 7737809375, 9509900499, 254803968, 19254145824, 19254145824, 345025251, 9509900499, 21003416576, 14693280768, 25937424601, 7737809375, 282475249, 282475249, 459165024, 312500000, 601692057, 30517578125]`

---

## Vulnerabilidades
Al observar los datos del reto, se pueden notar las siguientes anomalías en la "implementación personalizada" de RSA:

1.  **Tamaño del Ciphertext vs $n$:** Los números en la lista del `ciphertext` son extremadamente pequeños en comparación con el módulo $n$.
2.  **Cifrado por bloques/caracteres:** El ciphertext no es un único número gigante, sino una lista de números pequeños. Esto sugiere que el autor cifró partes del mensaje (o caracteres individuales) por separado.
3.  **El problema de $m^e < n$:** Si el mensaje original $m$ (o cada fragmento) es tan pequeño que al elevarlo a la quinta potencia ($m^5$) el resultado sigue siendo menor que $n$, entonces la operación de módulo no tiene efecto:
    $$c = m^e \pmod n \implies c = m^e$$
    Esto rompe la seguridad de RSA por completo.

---

## Resolucion
Para resolver este reto, los pasos a seguir serían:

1.  Identificar si efectivamente se cumple la condición de raíz directa ($m = \sqrt[e]{c}$).
2.  Desarrollar un script que aplique la raíz quinta exacta a cada elemento de la lista del ciphertext.
3.  Convertir los números resultantes (los mensajes en claro $m$) de vuelta a texto (ASCII / bytes).

---

## Script de Solución

este lo encontras en esta carpeta. el nombre es: 

---

##  The Flag: pecan{oh_i_really_thought_i_had_that_done_c0rr3ctly_11629}

---

## Tips
