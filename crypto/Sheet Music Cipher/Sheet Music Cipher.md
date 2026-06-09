# Sheet Music Cipher

## Detalles del Reto
| Atributo | Detalle |
| :--- | :--- |
| **Categoría** | Crypto |
| **Puntos** | 336 puntos |
| **Autor** | Raahguu |

---

## Descripción
> No one will ever know that I used a Compound Motivic Musical Cipher. I can merely play music out loud and send messages without anyone being any the wiser.

### Archivos del Reto
El reto nos provee un archivo que contiene la partitura:
* [`SheetMusicCipher.png`](./SheetMusicCipher.png)

---

## Vulnerabilidad

El reto se basa en la **Criptografía Musical**, específicamente utilizando variantes del **Método de J. Bücking**. A diferencia de otros métodos este utiliza un conjunto de notas con duraciones específicas para representar cada letra, el resultado es una melodía más larga y compleja.

Dentro de esta carpeta te dejo dos archivos extra,  [`metodo_thicknesse.png`](./metodo_thicknesse.png) es la clave de notas, pero ten en cuenta algunas cosa:
1. No solo basta con reemplazar las notas con letras.
2. Algunas notas estan de cabeza.
3. El truco es buscar palabras que ya conociamos.
Te dejo como lo resolvi, algunas partes estan mal, pero en general se entiende como reemplace cada letra.

---
## Flag

```text
pecan{buckingcipheriscooltoseeinaction}
