from main import Carpeta, CreadorPDF, CreadorTexto

def comprobar(nombre, esperado, obtenido):
    if esperado == obtenido:
        print("OK: " + nombre)
    else:
        print("FALLO: " + nombre + " | esperado =" + str(esperado) + " | obtenido =" + str(obtenido))

crear_pdf = CreadorPDF()
crear_texto = CreadorTexto()

# Caso 1: carpeta vacia
vacia = Carpeta("Vacia")
total = vacia.obtener_tamanio()
comprobar("Carpeta vacia", 0, total)

# Caso 2: carpeta con un PDF de 120
con_pdf = Carpeta("ConPDF")
con_pdf.agregar(crear_pdf.crear_archivo("Portal.pdf", 120))
total = con_pdf.obtener_tamanio()
comprobar("Carpeta con un PDF", 120, total)

# Caso 3: carpeta con PDF de 120 y texto de 80
con_ambos = Carpeta("ConPDF")
con_ambos.agregar(crear_pdf.crear_archivo("Portal.pdf", 120))
con_ambos.agregar(crear_texto.crear_archivo("Guia.txt", 80))
total = con_ambos.obtener_tamanio()
comprobar("Carpeta con un PDF y un txt", 200, total)

# Caso 4: ejemplo completo con subcarpeta de 50
con_todo = Carpeta("Valve")
con_todo.agregar(crear_pdf.crear_archivo("Portal.pdf", 120))
con_todo.agregar(crear_texto.crear_archivo("Guia.txt", 80))
sub = Carpeta("Laboratorio")
sub.agregar(crear_texto.crear_archivo("practica.txt", 50))
con_todo.agregar(sub)
total = con_todo.obtener_tamanio()
comprobar("Carpeta con un PDF y un txt y una subcarpeta", 250, total)

# Caso 5: carpeta con un archivo de tamaño 0
con_cero = Carpeta("ConPDF")
con_cero.agregar(crear_pdf.crear_archivo("Portal.pdf", 0))
total = con_cero.obtener_tamanio()
comprobar("Carpeta con un archivo de tamaño 0", 0, total)
