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

### Reconocimiento y Descarga
El script define una URL remota de un servidor de Comando y Control (C2) y localiza de forma dinámica la ruta de la carpeta de descargas del usuario utilizando objetos COM del sistema:

```powershell
$09c5b699434943b6b9a9ada620495bcb = "[http://192.168.126.148:8000/encrypted_flag.txt](http://192.168.126.148:8000/encrypted_flag.txt)"
$5a7e4a282bb7448fb7b5bfa39a35b0df = (Ne''w-Ob""jec''t -ComObject Shell.Application).Namespace('shell:Downloads').Self.Path
```

### La Función de Descifrado

El script expone la función `ded7e27bbf454228bcb53129ac07b6d1`, la cual es el núcleo del reto. En ella se observa una implementación de cifrado XOR simétrico:

```powershell
$339a18cced14be6bc35c6e7df638925 = 73 
foreach ($char in $f61e225cfe1d484981de4988b40df8b4.ToCharArray()) { 
    ... "-bxor" $339a18cced14be6bc35c6e7df638925 
}
```

* **Lectura:** Lee el archivo `encrypted_flag.txt`.
* **Proceso:** Itera carácter por carácter, convirtiéndolo a su valor entero.
* **Operación:** Aplica una operación XOR binaria (`-bxor`) utilizando una clave fija de valor `73`.

### Ejecución de la Carga Útil

El resultado de la función XOR se almacena en una variable y es ejecutado de forma inmediata en la memoria del sistema mediante el alias `Invoke-Expression` (`I''nvoke-Expr''ess""ion`). Esto significa que el archivo cifrado contiene código ejecutable u otra fase del script malicioso.

---

## Resolución 

Debido a que la operación XOR es simétrica (aplicar XOR dos veces con la misma clave regresa el texto original), podemos tomar el contenido cifrado de `encrypted_flag.txt` y aplicarle exactamente la misma llave `73` para revelar su contenido real.

Y como siempre, aqui esta el código:

**[`solve.py`](./solve.py)**

### Ejecución en la Terminal de Linux

```bash
python3 solve.py
```

### Flag

```text
pecan{0bfusc4t3d_c0d3_st111_w0rks_682374}
```
