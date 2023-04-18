import socket

# Host guardará la IP
# Ports guardará los puertos a escanear
host = input("Introduce la IP a escanear: ")
ports = input("Introduce los puertos a escanear (separados con coma): ")

#Esto va a separar los puertos que hemos leido por consola
ports = ports.split(",")

#Nos dice la cantidad de puertos guardados en la array ports
print(f"Se escanearán {len(ports)} puertos para la IP: {host}")

# Para cada puerto que haya en puertos
for puerto in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result= sock.connect_ex((host, int(puerto)))
    if result == 0:
        print(f"El puerto {puerto} está abierto")
    else:
        print(f"El puerto {puerto} está cerrado")
    sock.close()

    
    

