# Proyecto_Taller_Integrador_IS24

***Importante: Para la ejecución en tiempo real de la detección de placas es necesario correr el programa en una computadora que cuente con una tarjeta gráfica de Nvidia compatible con CUDA versión 12.1. De no contar con este hardware el rendimiento del programa no será suficiente para realizar la detección en tiempo real.***

## Pasos para la ejecución del programa
### 1. Instalar python versión 3.11.3
Para la descarga e instalación de Python puede referirse al siguiente *[enlace](https://www.python.org/downloads/release/python-3113/)*

***Es posible que el programa funcione con versiones más recientes de Python sin embargo se recomienda utilizar la versión 3.11.3***

### 2. Clonar la rama main de este repositorio
Se puede clonar el repositorio utilizando el método de referencia. Es recomendable colocar los archivos del repositorio clonado en una ruta que sea de "Fácil acceso" mediante la consola.

### 3. Instalar las dependencias del código
Por simplicidad las librerías necesarias junto con sus versiones están incluidas en el archivo llamado "requirements.txt".

Para su instalación, utilizando un terminal (como cmd o Windows Powershell) se debe ingresar al directorio en el cual se encuentran los archivos clonados del repositorio. Una vez en dicho directorio se debe ejecutar el comando:

***pip install -r requirements.txt***

Esto instalará las librerías necesarias, proceso que puede tardar algunos minutos.

### 4. Modificar el código para obtener acceso a la transmisión de video de la cámara
Para poder accesar al video proveniente desde la cámara con el programa es necesario realizar una modificación en el archivo "main.py". Para esto se debe abir el archivo "main.py" utilizando del IDE de python o algún otro editor de texto de su preferencia y se debe buscar la línea 11 de código la cual contiene la siguiente instrucción:

***video = cv2.VideoCapture('protocolo://username:password@direccion_ip')***

Esta línea se da como ejemplo y no tiene la capacidad de accesar al stream de video de la cámara. Para lograr esto se deben modificar los parámetros "protocolo://username:password@direccion_ip" de la siguiente manera:
- En protocolo se debe ingresar el protocolo utilizado por la cámara, usualmente ***RTSP*** o ***HTTP***.
- En username se debe ingresar el nombre de usuario necesario para acceder al stream de video, nótese los caracteres "://" que dividen el espacio del protocolo y el username.
- En password se debe ingresar la contraseña para acceder a la cámara, nuevamente nótese el caracter ":" presente entre username y password.

downgroudear cuda
instalar torch a la fuerza

