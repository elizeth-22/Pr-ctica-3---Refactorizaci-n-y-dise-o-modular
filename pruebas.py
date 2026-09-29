from main import Carpeta, agregar_archivo, obtener_tamanio

def comprobar(nombre, esperado, obtenido):
    if esperado == obtenido:
        print("OK: " + nombre)
    else:
        print("FALLO: " + nombre + " | esperado =" + str(esperado) + " | obtenido =" + str(obtenido))

# Caso 1: carpeta vacia
vacia = Carpeta("Vacia")
total = obtener_tamanio(vacia)
comprobar("Carpeta vacia", 0, total)

# Caso 2: carpeta con un PDF de 120
con_pdf = Carpeta("ConPDF")
agregar_archivo(con_pdf, "pdf", "Portal.pdf", 120)
total = obtener_tamanio(con_pdf)
comprobar("Carpeta con un PDF", 120, total)

# Caso 3: carpeta con PDF de 120 y texto de 80
con_ambos = Carpeta("ConPDF")
agregar_archivo(con_ambos, "pdf", "Portal.pdf", 120)
agregar_archivo(con_ambos, "txt", "Guia.txt", 80)
total = obtener_tamanio(con_ambos)
comprobar("Carpeta con un PDF y un txt", 200, total)

# Caso 4: ejemplo completo con subcarpeta de 50
con_todo = Carpeta("Valve")
agregar_archivo(con_todo, "pdf", "Portal.pdf", 120)
agregar_archivo(con_todo, "txt", "Guia.txt", 80)
sub = Carpeta("Laboratorio")
agregar_archivo(sub, "txt", "practica.txt", 50)
con_todo.subcarpetas.append(sub)
total = obtener_tamanio(con_todo)
comprobar("Carpeta con un PDF y un txt y una subcarpeta", 250, total)

# Caso 5: carpeta con un archivo de tamaño 0
con_pdf = Carpeta("ConPDF")
agregar_archivo(con_pdf, "pdf", "Portal.pdf", 0)
total = obtener_tamanio(con_pdf)
comprobar("Carpeta con un archivo de tamaño 0", 0, total)
