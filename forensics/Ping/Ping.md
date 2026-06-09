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

A simple vista, al inspeccionar el tráfico en Wireshark, no observamos nada fuera de lo comun en las direcciones IP, puertos ni en el protocolo. 


<img width="960" height="302" alt="image" src="https://github.com/RatonBri/ICOA2026resolucion/blob/main/forensics/Ping/Captura%20de%20pantalla%202026-06-09%20112654.png"/>


Sin embargo, al analizar minuciosamente cada paquete, un pequeño detalle nos llama la atención: **la longitud del mensaje (`Data Length`) cambia en cada paquete**.

Al principio, estos tamaños podrían parecer valores aleatorios asignados por el sistema, pero si se conocen los fundamentos del alfabeto **ASCII**, se puede identificar un patrón directo:
* En el paquete de la imagen, la longitud de la data es exactamente **112**.
* En la tabla ASCII, el número decimal `112` corresponde a la letra **`p`**, que es el carácter inicial de la flag (`pecan{`).

<img width="1907" height="646" alt="image" src="https://github.com/RatonBri/ICOA2026resolucion/blob/main/forensics/Ping/Captura%20de%20pantalla%202026-06-09%20115611.png" />

El atacante está aplicando una técnica de exfiltración de información ocultando un carácter por cada paquete transmitido dentro del metadato de longitud. 

> **Nota Crítica de Ordenamiento:** Para reconstruir la bandera sin corromper el mensaje, **no se debe modificar el orden predeterminado** de los paquetes en la captura. Si se altera la secuencia nativa, las letras se mezclarán y será mas complicado reordenarlas.

---

## Resolución y Comandos en Linux

Para resolver este reto mucho mas rapido sin estar anotando y convirtiendo a mano cada caracter, empleamos la herramienta `tshark` desde Linux, para extraer los tamaños y procesarlos en una sola línea de comandos.

### Extracción de las Longitudes de los Paquetes
Primero, utilizamos `tshark` para filtrar los paquetes de petición ICMP (Echo Request) e imprimir en pantalla únicamente el valor numérico de la longitud de su campo de datos:

```bash
tshark -r capture.pcapng -Y "icmp.type == 8" -T fields -e data.len
```

#### Componentes del Comando

* **`-r capture.pcapng`**
  Lee el archivo de la captura de red especificado.
* **`-Y "icmp.type == 8"`**
  Filtra para mostrar solo paquetes ICMP *Echo Request* (pings de ida).
* **`-T fields`**
  Indica que se extraerá información de campos específicos del paquete.
* **`-e data.len`**
  Selecciona exclusivamente el campo que contiene la longitud de los datos.

### Conversión de Decimal a ASCII

Para evitar traducir los números uno por uno, conectamos la salida del comando anterior. Esto traduce de forma inmediata los valores decimales a texto legible:

```bash
tshark -r capture.pcapng -Y "icmp.type == 8" -T fields -e data.len | awk '{printf "%c", $1}'
```

#### Componentes del Comando

 * **`| awk '{printf "%c", $1}'`**
   Toma cada número, lo convierte a su carácter ASCII correspondiente (`%c`) y los imprime de corrido en una sola línea para revelar el texto oculto.

---

## Flag

```text
pecan{d4t4_3xf1ltr4t10n_thr0gh_p1ng_93485}





