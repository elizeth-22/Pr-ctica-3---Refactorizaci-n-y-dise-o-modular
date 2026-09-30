#Codigo de la practica 3: se esta refactorizando jeje

class Elemento:
    def obtener_tamanio(self):
        pass
    
class Archivo(Elemento):
    def __init__(self, nombre, tamanio):
        self.nombre = nombre
        self.tamanio = tamanio
    def obtener_tamanio(self):
        return self.tamanio


class ArchivoPDF(Archivo):
    def __init__(self, nombre, tamanio):
        super().__init__(nombre, tamanio)


class ArchivoTexto(Archivo):
    def __init__(self, nombre, tamanio):
        super().__init__(nombre, tamanio)


class Carpeta(Elemento):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []
    def obtener_tamanio(self):
        total = 0
        for elemento in self.elementos:
            total += elemento.obtener_tamanio()
        return total
    def agregar(self, elemento):
        self.elementos.append(elemento)
        


class CorreoLegacy:
    def send_email(self, to, body):
        print("Para: " + to)
        print(body)


def agregar_archivo(carpeta, tipo, nombre, tamanio):
    if tipo == "pdf":
        carpeta.agregar(ArchivoPDF(nombre, tamanio))
    elif tipo == "txt":
        carpeta.agregar(ArchivoTexto(nombre, tamanio))

def obtener_tamanio(carpeta):
    total = 0
    for archivo in carpeta.archivos:
        total += archivo.tamanio
    for subcarpeta in carpeta.subcarpetas:
        total += obtener_tamanio(subcarpeta)
    return total


def enviar_resultado(carpeta, destino):
    correo = CorreoLegacy()
    correo.send_email(destino, "Tamanio total: " + str(carpeta.obtener_tamanio()))


def main():
    clase = Carpeta("MyP")
    agregar_archivo(clase, "pdf", "practica.pdf", 120)
    agregar_archivo(clase, "txt", "notas.txt", 80)

    ejemplos = Carpeta("Ejemplos")
    agregar_archivo(ejemplos, "txt", "ejemplo.txt", 50)
    clase.agregar(ejemplos)

    print(clase.obtener_tamanio())
    enviar_resultado(clase, "profesor@universidad.edu")


if __name__ == "__main__":
    main()
