## Analisis de métodos
1. El método agregar_archivo se encarga de:<br>
Revisa el tipo del archivo, (.pdf o .txt), y crea un objeto de la clase 
correspondiente junto a su nombre y tamaño, y luego lo guarda en la lista de 
archivos de la carpeta

2. El método obtener_Tamanio se encarga de:<br>
Calcula el tamaño total de una carpeta: suma el tamaño de sus archivos y, por 
cada subcarpeta, usa recursión para sumar también lo que contiene, sin 
importar cuántos niveles de subcarpetas haya. Devuelve ese total

3. El método enviar_resultado se encarga de:<br>
Calcula el tamaño total de una carpeta usando el método de obtener y simula
un envio por email; arma la estructura del mensaje: "Tamanio total: ", después
crea un objeto LegacyCorreo y lo "envia" usando send_email

## Problemas
1. **Creación de archivos**<br>
- Donde aparece: en agregar_archivo<br>
- Que cambio sería dificil: agregar un tipo nuevo de archivo, ya que se debe de
modificar el metodo antes mencionado añadiendo un nuevo if, ademas de tener que
crear una nueva clase para este nuevo tipo de archivo<br>
- Que clase podría hacerse responsable: Una nueva clase creadora del nuevo tipo
de archivos<br>

2. **Calcular tamaño**<br>
- Donde aparece: en obtener_tamanio, tiene un for distinto para archivos y otro 
para subcarpetas, y en Carpeta ya que tiene una lista distinta para cada tipo
de organizador<br>
- Que cambio seria dificil: agregar un nuevo tipo de organización (ademas de 
archivo y carpeta), porque se tiene que crear otra lista en Carpeta y un nuevo
for en obtenerTamanio<br>
- Que clase podria hacerse responsable: una interfaz en comun con obtenerTamanio
que implementen Carpeta y Archivo<br>

3. **Envio de correo**<br>
- Donde aparece: en enviar_resultado, que llama a send_email de legacyCorreo<br>
- Que cambio seria dificil: que se cambie el servicio de correo, ya que el metodo
de enviarResultado depende de un metodo con un nombre específico. Habria que 
editar enviarResultado si llega a cambiar ese metodo<br>
- Que clase podría hacerse responsable: una nueva interfaz que implemente un 
metodo llamado enviar por ejemplo, y una clase intermedia que traduzca enviar a
sendEmail. El programa solo se relaciona con esa interfaz evitando problemas 
si se cambia el servicio de correo <br>

## Cambios realizados

**Composite:** <br>
Se creo la superclase `Elemento` con `obtener_tamanio()`. `Archivo`
y `Carpeta` la implementan: el archivo devuelve su tamaño y la carpeta suma lo
que le devuelve cada elemento que contiene. `Carpeta` ahora guarda todo en una
sola lista (en lugar de dos) y tiene el método `agregar`.
<br>
**Factory Method:**<br> 
Se creo `CreadorArchivo` con `crear_archivo(nombre, tamanio)`y sus dos 
subclases, `CreadorPDF` y `CreadorTexto`. Cada una devuelve su tipo de archivo.
Se eliminó `agregar_archivo` y su `if/elif`. Ahora el creador construye el 
archivo y la carpeta lo guarda con `agregar`.
<br>
**Adapter:** <br>
Se creo `Notificador` con `enviar(destino, mensaje)` y `AdaptadorCorreo`, que 
guarda un `CorreoLegacy` y traduce `enviar` a `send_email`. `enviar_resultado` 
ahora recibe un `Notificador` como parámetro,en lugar de crear el 
`CorreoLegacy` directamente. `CorreoLegacy` no se modificó.
<br>

## Diagrama final

    Elemento  <-- Archivo  <-- ArchivoPDF
    Elemento  <-- Archivo  <-- ArchivoTexto
    Elemento  <-- Carpeta

    CreadorArchivo <-- CreadorPDF   --> ArchivoPDF
    CreadorArchivo <-- CreadorTexto --> ArchivoTexto

    Notificador <-- AdaptadorCorreo -->> CorreoLegacy

Simbología: <br>
`<--` es herencia (la clase de la derecha hereda de la de la izquierda).<br> 
`-->` indica que el creador construye ese objeto.<br>
`-->>` indica que el adaptador llama a esa clase.<br>

## Responsabilidades

**Qué se movió en cada clase:**
- Calcular el tamaño: antes lo hacía una función de afuera, ahora lo hace cada
  Archivo y cada Carpeta.
- Crear archivos: antes lo hacia `agregar_archivo`, ahora lo hacen
  `CreadorPDF` y `CreadorTexto`.
- Guardar archivos: ahora solo lo hace `Carpeta` con `agregar`.
- Conectar con el correo: antes lo hacía `enviar_resultado`, ahora lo hace
  `AdaptadorCorreo`.

**Qué permaneció igual:** 
La salida del programa (el 250 y el correo simulado). <br>

## Pruebas

| Prueba | Entrada | Esperado | Obtenido antes | Antes | Obtenido después | Después |
|---|---|---|---|---|---|---|
| 1 | Carpeta vacía | 0 | 0 | OK | 0 | OK |
| 2 | Carpeta con un PDF de 120 | 120 | 120 | OK | 120 | OK |
| 3 | Carpeta con PDF de 120 y texto de 80 | 200 | 200 | OK | 200 | OK |
| 4 | Carpeta con PDF de 120, texto de 80 y subcarpeta con texto de 50 | 250 | 250 | OK | 250 | OK |
| 5 | Carpeta con un archivo de tamaño 0 | 0 | 0 | OK | 0 | OK |