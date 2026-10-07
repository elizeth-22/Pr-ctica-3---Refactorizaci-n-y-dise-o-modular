#Codigo de la practica 3: ya está refacorizado yei :b

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

class CreadorArchivo:
    def crear_archivo(self, nombre, tamanio):
        pass

class CreadorPDF(CreadorArchivo):
    def crear_archivo(self, nombre, tamanio):
        return ArchivoPDF(nombre, tamanio)

class CreadorTexto(CreadorArchivo):
    def crear_archivo(self, nombre, tamanio):
        return ArchivoTexto(nombre, tamanio)

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

# Adapter{
class Notificador:
    def enviar(self, destino, mensaje):
        pass 

class AdaptadorCorreo(Notificador):
    def __init__(self, correo):
        self.correo = correo
    def enviar(self, destino, mensaje):
        self.correo.send_email(destino, mensaje)
#}
#Modifiacion de Adapter a este metodo
def enviar_resultado(carpeta, destino, notificador):
    notificador.enviar(destino, "Tamanio total: " + str(carpeta.obtener_tamanio()))


def main():
    crear_pdf = CreadorPDF()
    crear_texto = CreadorTexto()

    clase = Carpeta("MyP")
    clase.agregar(crear_pdf.crear_archivo("practica.pdf", 120))
    clase.agregar(crear_texto.crear_archivo("notas.txt", 80))

    ejemplos = Carpeta("Ejemplos")
    ejemplos.agregar(crear_texto.crear_archivo("ejemplo.txt", 50))
    clase.agregar(ejemplos)

    print(clase.obtener_tamanio())

    adaptador = AdaptadorCorreo(CorreoLegacy())
    enviar_resultado(clase, "profesor@universidad.edu", adaptador)


if __name__ == "__main__":
    main()
