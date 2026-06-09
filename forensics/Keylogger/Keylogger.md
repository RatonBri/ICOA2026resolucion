# Keylogger

## Detalles del Reto
| Atributo | Detalle |
| :--- | :--- |
| **Categoría** | Forensics / Reverse Engineering |
| **Puntos** | 264 puntos |
| **Autor** | Viet Huy Nguyen |

---

## Descripción
> After sensing that something was not right, Ole reported it to the security team. The team decided to investigate the network and noticed something suspicious.

### Archivos Provistos
* **Archivo:** [`capture.pcapng`](./capture.pcapng)

---

## Análisis

### 1. Inspección del Tráfico en Wireshark
Analizamos los flujos de comunicación dentro del archivo de red. Aplicamos un filtro de visualización en Wireshark para aislar el tráfico HTTP e identificar descargas de archivos sospechosas:

```text
tcp.stream eq 1
```

De entre ellos, el más resaltante es este: 

```text
GET /keylogger.py HTTP/1.1
```

### ¿Por qué seleccionamos el paquete GET?

El método HTTP `GET` indica que el cliente (la máquina víctima) solicitó un recurso al servidor del atacante. Al inspeccionar este flujo, encontramos la petición exacta `GET /keylogger.py HTTP/1.1` ejecutada desde una terminal de PowerShell (identificada en el `User-Agent`).

El servidor web del atacante (`SimpleHTTP/0.6 Python/3.12.7`) respondió con un estado `200 OK` y transfirió el código fuente completo de un script de Python. Al seguir el flujo TCP (**Follow TCP Stream**), pudimos extraer el código del malware para analizar su comportamiento.

---

### Ingeniería Inversa del Keylogger (keylogger.py)

Al examinar el código capturado, confirmamos que se trata de un software espía (*Spyware/Keylogger*) diseñado para registrar las pulsaciones del teclado de la víctima durante un intervalo de 30 segundos (`duration = 30`). Su flujo lógico se divide en tres fases críticas:

#### A. Estructura de la Codificación Ofuscada
El atacante implementó un algoritmo de sustitución personalizado dentro de la función `Encode()` para evitar que las pulsaciones del teclado fueran legibles en texto plano al viajar por la red, evadiendo así sistemas de detección de intrusos (IDS):

* **`array64`:** Contiene el alfabeto ordenado empleado de forma estándar para la codificación Base64 (`abcdef...0123456789/+=`).
* **`cipher`:** Una lista estática indexada que contiene 92 palabras comunes o contraseñas en inglés (como *"password"*, *"123456789"*, *"sunshine"*, etc.).

#### B. El Mecanismo de Codificación (Encode)

```python
def Encode():
    payloadFile = open(output_file, 'rb')
    payloadRaw = payloadFile.read()
    payloadB64 = base64.b64encode(payloadRaw)
    with open(encoded_output_file, "w") as file:
        for byte in payloadB64:
            if byte != '\n':
                file.write(cipher[array64.index(chr(byte))] + '\n')
```

##### ¿Cómo funciona este cifrado paso a paso?
1. El malware toma el archivo con las teclas capturadas (`keystroke.txt`) y lo convierte a Base64.
2. Lee cada carácter resultante de ese bloque Base64 y busca en qué posición numérica (índice) se encuentra dentro de la lista `array64`.
3. Utiliza ese mismo índice numérico para extraer una palabra completa de la lista `cipher` y la escribe en un nuevo archivo (`keystroke_encoded.txt`), separando cada palabra con un salto de línea (`\n`).

#### C. Fase de Exfiltración (transfer_file)
Una vez codificado el archivo, la función `transfer_file()` levanta un socket de escucha TCP en el puerto local `1234` de la máquina comprometida (`192.168.126.129`). En cuanto el atacante se conecta a ese puerto, el script le transmite todo el diccionario de palabras generadas.

---

### Estrategia de Solución (Ingeniería Inversa)

Debido a que el algoritmo de cifrado es determinista y utiliza matrices con posiciones fijas, el proceso es completamente reversible si seguimos el camino inverso:

* **Extraer los datos de la red:** Leemos la captura de red utilizando la librería `scapy` de Python para recuperar las palabras consecutivas enviadas a través de los paquetes (`Raw Payload`).
* **Segmentar el texto:** Dividimos el flujo de texto por sus saltos de línea para aislar cada palabra del diccionario `cipher`.
* **Mapeo de Índices:** Buscamos la posición de cada palabra dentro de `cipher` para obtener su índice numérico.
* **Reconstrucción Base64:** Usamos ese índice para extraer el carácter equivalente de `array64` y reconstruir la cadena Base64 original.
* **Decodificación Final:** Traducimos el Base64 resultante para revelar el texto plano con las pulsaciones reales de la víctima.

### Script de Solución

Este fue un poco mas complicado de realizar 

---

## Flag

```text
pecan{k3ylogger_p3c4n_2025}
