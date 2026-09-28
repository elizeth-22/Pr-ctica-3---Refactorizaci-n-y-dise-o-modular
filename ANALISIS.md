1. El método agregarArchivo se encarga de:
Revisa el tipo del archivo, (.pdf o .txt), y crea un objeto de la clase 
correspondiente junto a su nombre y tamaño, y luego lo guarda en la lista de 
archivos de la carpeta

2. El método obtenerTamanio se encarga de:
Calcula el tamaño total de una carpeta: suma el tamaño de sus archivos y, por 
cada subcarpeta, usa recursión para sumar también lo que contiene, sin 
importar cuántos niveles de subcarpetas haya. Devuelve ese total

3. El método enviarResultado se encarga de:
Calcula el tamaño total de una carpeta usando el método de obtener y simula
un envio por email; arma la estructura del mensaje: "Tamanio total: ", después
crea un objeto CorreoLegacy y lo "envia" usando sendEmail