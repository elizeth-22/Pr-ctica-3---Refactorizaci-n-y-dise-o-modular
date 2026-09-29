##Analisis de métodos
1. El método agregarArchivo se encarga de:<br>
Revisa el tipo del archivo, (.pdf o .txt), y crea un objeto de la clase 
correspondiente junto a su nombre y tamaño, y luego lo guarda en la lista de 
archivos de la carpeta

2. El método obtenerTamanio se encarga de:<br>
Calcula el tamaño total de una carpeta: suma el tamaño de sus archivos y, por 
cada subcarpeta, usa recursión para sumar también lo que contiene, sin 
importar cuántos niveles de subcarpetas haya. Devuelve ese total

3. El método enviarResultado se encarga de:<br>
Calcula el tamaño total de una carpeta usando el método de obtener y simula
un envio por email; arma la estructura del mensaje: "Tamanio total: ", después
crea un objeto CorreoLegacy y lo "envia" usando sendEmail

##Problemas
1. Creación de archivos<br>
Donde aparece: en agregarArchivo<br>
Que cambio sería dificil: agregar un tipo nuevo de archivo, ya que se debe de
modificar el metodo antes mencionado añadiendo un nuevo if, ademas de tener que
crear una nueva clase para este nuevo tipo de archivo<br>
Que clase podría hacerse responsable: Una nueva clase creadora del nuevo tipo
de archivos<br>

2. Calcular tamaño<br>
Donde aparece: en ontenerTamanio, tiene un for distinto para archivos y otro 
para subcarpetas, y en Carpeta ya que tiene una lista distinta para cada tipo
de organizador<br>
Que cambio seria dificil: agregar un nuevo tipo de organización (ademas de 
archivo y carpeta), porque se tiene que crear otra lista en Carpeta y un nuevo
for en obtenerTamanio<br>
Que clase podria hacerse responsable: una interfaz en comun con obtenerTamanio
que implementen Carpeta y Archivo<br>

3. Envio de correo<br>
Donde aparece: en enviarResultado, que llama a sendEmail de legacyCorreo<br>
Que cambio seria dificil: que se cambie el servicio de correo, ya que el metodo
de enviarResultado depende de un metodo con un nombre específico. Habria que 
editar enviarResultado si llega a cambiar ese metodo<br>
Que clase podría hacerse responsable: una nueva interfaz que implemente un 
metodo llamado enviar por ejemplo, y una clase intermedia que traduzca enviar a
 sendEmail. El programa solo se relaciona con esa interfaz evitando problemas 
 si se cambia el servicio de correo <br>