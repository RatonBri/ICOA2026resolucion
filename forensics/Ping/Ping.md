# Ping

## Detalles del Reto
| Atributo | Detalle |
| :--- | :--- |
| **Categoría** | Networking / Forensics |
| **Puntos** | 208 puntos |
| **Autor** | Viet Huy Nguyen |

---

## Descripción
> Attackers are getting clever these days, they're finding all sorts of ways to exfiltrate data! What did they steal this time?

### Archivos Provistos
* **Archivo:** [`capture.pcapng`](./capture.pcapng)

---

## Vulnerabilidad

A simple vista, al inspeccionar el tráfico en Wireshark, no observamos nada fuera de lo comun en las direcciones IP, puertos ni en el protocolo. Sin embargo, al analizar minuciosamente cada paquete, un pequeño detalle nos llama la atención: **la longitud del mensaje (`Data Length`) cambia en cada paquete**.

Al principio, estos tamaños podrían parecer valores aleatorios asignados por el sistema, pero si se conocen los fundamentos del alfabeto **ASCII**, se puede identificar un patrón directo:
* En el paquete de la imagen, la longitud de la data es exactamente **112**.
* En la tabla ASCII, el número decimal `112` corresponde a la letra **`p`**, que es el carácter inicial de la flag (`pecan{`).

El atacante está aplicando una técnica de exfiltración de información ocultando un carácter por cada paquete transmitido dentro del metadato de longitud. 

> **Nota Crítica de Ordenamiento:** Para reconstruir la bandera sin corromper el mensaje, **no se debe modificar el orden predeterminado** de los paquetes en la captura. Si se altera la secuencia nativa, las letras se mezclarán y será imposible descifrar la palabra original.

---

## Resolución y Comandos en Linux

Para resolver este reto de forma automatizada desde la terminal de Linux, empleamos la herramienta `tshark` para extraer los tamaños y procesarlos en una sola línea de comandos.

### Paso 1: Extracción de las Longitudes de los Paquetes
Primero, utilizamos `tshark` para filtrar los paquetes de petición ICMP (Echo Request) e imprimir en pantalla únicamente el valor numérico de la longitud de su campo de datos:

```bash
tshark -r capture.pcapng -Y "icmp.type == 8" -T fields -e data.len















a simple vista no hay nada resalte en los datos de winsahr, ni en el destino ni protocolo, pero algo que nos llama la atenciaon al ver cada paquete es la dat del mensaje, 
principalmente la longitud de cada mensaje, si nos fijamos, cambia entre cada pauqte, al inicio pareciera que son solo datos al aar, pero si conoces el alfabeto ascii reconoceremos que p equivale al 112, 
esto es la calve de todo, verificamos los siguientes paquetes y listo, tenemos nuetsra flag, pero para quie obtengas la bandera sin ningun problema, no debes moificar el orden predetermiando, si cambias dicho orden se complicara ordenar las palabras.




<img width="960" height="302" alt="image" src="https://github.com/user-attachments/assets/24705823-dd3e-47ef-914a-f1d257829477" />



<img width="1907" height="646" alt="image" src="https://github.com/user-attachments/assets/b9789515-8dd2-4464-9fe7-772c85b5c4d3" />
