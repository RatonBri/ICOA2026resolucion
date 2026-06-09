import base64
from scapy.all import rdpcap

cipher = [
    "password", "123456789", "sunshine", "qwerty", "iloveyou", "princess", "admin", "welcome",
    "666666", "abc123", "football", "monkey", "654321", "!@#$%^&*", "charlie", "aa123456",
    "donald", "password1", "qwerty123", "letmein", "zxcvbnm", "login", "starwars", "121212",
    "bailey", "freedom", "shadow", "passw0rd", "master", "baseball", "buster", "Daniel",
    "Hannah", "Thomas", "summer", "George", "Harley", "222222", "Jessica", "ginger", "abcdef",
    "Jordan", "55555", "Tigger", "Joshua", "Pepper", "Robert", "Matthew", "Andrew", "lakers",
    "andrea", "1qaz2wsx", "sophie", "Ferrari", "Cheese", "Computer", "jesus", "Corvette",
    "Mercedes", "flower", "Blahblah", "Maverick", "Hello", "loveme", "nicole", "hunter",
    "amanda", "jennifer", "banana", "chelsea", "ranger", "trustno1", "merlin", "cookie",
    "ashley", "bandit", "killer", "aaaaaa", "1q2w3e", "zaq1zaq1", "mustang", "test",
    "hockey", "dallas", "whatever", "admin123", "michael", "liverpool", "querty", "william",
    "soccer", "london"
]
array64 = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/+=")

def descifrar_reto(pcap_file):
    # Extrae el texto manteniendo los saltos de línea intactos
    texto_recibido = ""
    for pkt in rdpcap(pcap_file):
        if pkt.haslayer('Raw'):
            texto_recibido += pkt['Raw'].load.decode('utf-8', errors='ignore')

    # Separa las palabras por líneas y limpia espacios
    palabras = [p.strip() for p in texto_recibido.split('\n') if p.strip()]

    # Reconstruye la cadena Base64 mapeando cada palabra con cipher
    base64_reconstruido = "".join(array64[cipher.index(p)] for p in palabras if p in cipher)

    # Añade el relleno necesario de Base64
    base64_reconstruido += "=" * ((4 - len(base64_reconstruido) % 4) % 4)

    # Decodifica e imprime el resultado final directamente
    print(base64.b64decode(base64_reconstruido).decode('utf-8', errors='ignore'))

descifrar_reto("captured.pcapng")
