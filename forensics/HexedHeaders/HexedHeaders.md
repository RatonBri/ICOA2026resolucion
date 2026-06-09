# HexedHeaders

## Detalles del Reto
| Atributo | Detalle |
| :--- | :--- |
| **Categoría** | Forensics |
| **Puntos** | 144 puntos |
| **Autor** | Riley Grimwood |

---

## Descripción
> This file seems to contain secrets... But how to get in...

### Archivos Provistos
* **Archivo:** [`pecanctflogo.jpg`](./pecanctflogo.jpg)
---

## Explicación Técnica del Problema

El reto consiste en una **falsificación de Magic Bytes (Cabeceras de Archivo)**. El autor tomó un archivo JPEG real pero modificó manualmente sus primeros 8 bytes inyectándole la firma de un archivo PNG (`89 50 4E 47 0D 0A 1A 0A`).

Cuando un software intenta abrir la imagen, lee los primeros bytes, asume erróneamente que es un PNG y trata de decodificarlo como tal. Sin embargo, al avanzar en el archivo encuentra marcadores e información estructurada de formato JPEG (`JFIF`), provocando que el programa falle y devuelva un error de archivo corrupto.

---

## Resoluión

### Inspección del Archivo Binario
Asi es como puedes comprobar lo que afirme al inicio, para ello revisamos los magic bytes:

```bash
xxd pecanctflogo.jpg | head -n 1
```

#### Componentes del Comando

* **`xxd`**
  Transforma archivos binarios en volcados hexadecimales legibles.
* **`pecanctflogo.jpg`**
  El archivo objetivo que se va a inspeccionar.
* **`|` (Pipe / Tubería)**
  Envía la salida izquierda hacia la entrada derecha.
* **`head -n 1`**
  Muestra únicamente la primera línea del volcado resultante.


Nos da como respuesta:

```bash
00000000: 8950 4e47 0d0a 1a0a 0010 4a46 4946 0001  .PNG......JFIF..
```

Aqui ya es mas claro, nos indican que es un archivo png, los magic bytes lo muestran, pero mas adelante en el cuerpo de tu archivo, no parece ser una imágen en formato png.


### Reemplazo de Cabecera

Ya sabiendo que necesitamos corregir la cabecera del archivo, utilizamos el siguiente comando, reemplazará los magic bytes de la imagen por los correctos, perteneciente a un jpg.

```bash
xxd -p pecanctflogo.jpg | sed 's/^89504e470d0a1a0a/ffd8ffe000104a46/' | xxd -r -p > imagen_solucion.jpg
```

#### Componentes del Comando

* **`xxd -p pecanctflogo.jpg`**
  Vuelca el archivo en formato hexadecimal continuo, sin direcciones ni traducción ASCII.
* **`sed 's/^89504e470d0a1a0a/ffd8ffe000104a46/'`**
  Editor de flujo que busca la firma corrupta de PNG al inicio (`^`) y la reemplaza por la de JPEG.
* **`xxd -r -p`**
  Revierte el proceso (`-r`), convirtiendo el texto hexadecimal plano (`-p`) de vuelta a datos binarios puros.
* **`> imagen_solucion.jpg`**
  Redirige y guarda el binario corregido en un nuevo archivo de imagen.


Listo, ya nos dio la bandera, solo debes abrir la iamgen generada.

---

## Flag

```text
pecan{h3x_and_hea43r2}
