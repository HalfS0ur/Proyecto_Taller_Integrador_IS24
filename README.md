# Proyecto_Taller_Integrador_IS24

***Importante: Para la ejecución en tiempo real de la detección de placas es necesario correr el programa en una computadora que cuente con una tarjeta gráfica de Nvidia compatible con CUDA versión 12.1, preferiblemente con memoria VRAM mayor o igual a 8 GB y utilizando arquitectura Turing o más reciente (Puede consultar más información sobre CUDA en este [enlace](https://en.wikipedia.org/wiki/CUDA#GPUs_supported) y sobre modelos con arquitectura Turing en este [enlace](https://en.wikipedia.org/wiki/Turing_(microarchitecture))). De no contar con este hardware el rendimiento del programa no será suficiente para realizar la detección en tiempo real.***

## Pasos para la ejecución del programa
### 1. Instalar python versión 3.11.3
Para la descarga e instalación de Python puede referirse al siguiente *[enlace](https://www.python.org/downloads/release/python-3113/)*

***Es posible que el programa funcione con versiones más recientes de Python sin embargo se recomienda utilizar la versión 3.11.3***

### 2. Clonar la rama main de este repositorio
Se puede clonar el repositorio utilizando el método de referencia. Es recomendable colocar los archivos del repositorio clonado en una ruta que sea de "fácil acceso" mediante la terminal.

### 3. Instalar las dependencias del código
Por simplicidad las librerías necesarias junto con sus versiones están incluidas en el archivo llamado "requirements.txt".

Para su instalación, utilizando un terminal (como cmd o Windows Powershell) se debe ingresar al directorio en el cual se encuentran los archivos clonados del repositorio. Una vez en dicho directorio se debe ejecutar el comando:

***pip install -r requirements.txt***

Esto instalará las librerías necesarias, proceso que puede tardar algunos minutos.

### 4. Modificar el código para obtener acceso a la transmisión de video de la cámara
Para poder accesar al video proveniente desde la cámara con el programa es necesario realizar una modificación en el archivo "main.py". Para esto se debe abir el archivo "main.py" utilizando del IDE de python o algún otro editor de texto de su preferencia y se debe buscar la línea 11 de código la cual contiene la siguiente instrucción:

***video = cv2.VideoCapture('protocolo://username:password@direccion_ip')***

Esta línea se da como ejemplo y debe ser modificada para lograr accesar el stream de video de la cámara. Para ello se deben modificar los parámetros "protocolo://username:password@direccion_ip" de la siguiente manera:
- En protocolo se debe ingresar el protocolo utilizado por la cámara, usualmente ***RTSP*** o ***HTTP***.
- En username se debe ingresar el nombre de usuario necesario para acceder al stream de video, nótese los caracteres "://" que dividen el espacio del protocolo y el username.
- En password se debe ingresar la contraseña para acceder a la cámara, nuevamente nótese el caracter ":" presente entre username y password.
- Finalmente, en dirección_ip se debe ingresar la dirección ip correspondiente a la cámara que se desea utilizar con el programa. Nótese el caracter "@" que separa la dirección_ip y password.
  
De esta manera si se tuviera una cámara que utiliza el protocolo RTSP, con un username "usuario", password "contraseña" y dirección ip 1.2.3.4/5 se debería modificar la línea 11 de la siguiente manera:

***video = cv2.VideoCapture('RTSP://usuario:contraseña@1.2.3.4/5')***

***Importante:*** Dependiendo de la configuración de red utilizada, es posible que la computadora utilizada para correr el programa necesite permisos especiales del administrador de la red para poder accesar a los streams de video de las cámaras conectadas a la red.

### 5. Ejecutar el programa
Una vez seguidos los pasos anteriores se puede ejecutar el programa ya sea abriendo el archivo "main.py" en el editor de python y presionando la tecla F5 o bien, utilizando un terminal (como cmd o Windows Powershell) se puede ingresar al directorio en el cual se encuentran los archivos clonados del repositorio y se debe ejecutar el comando ***python main.py*** para ejecutar el programa.

***Importante:*** Durante la primera ejecución se requiere una conexión a internet para que la librería EasyOCR pueda descargar los modelos de detección de caracteres, lo cual puede tardar algunos minutos.

## Posibles problemas durante la ejecución del programa
### Mensaje de error: Cuda isn't available. Using CPU. Note: This module is much faster with a GPU.
Este mensaje de error viene acompañado de un bajo rendimiento del programa al momento de analizar y procesar el video y se debe a que la versión de CUDA instalada no es compatible con Pytorch, una librería necesaria para el funcionamiento de la librería YOLO.

Es posible verificar la incompatibilidad con la versión de CUDA ejecutando los siguientes comandos en una consola ***uno a uno***:
- python
- import torch
- torch.cuda.is_available()

Si la consola retorna el mensaje "False" existe una incompatibilidad entre CUDA y Pytorch.

Para solucionar este problema primero se deben desinstalar las versiones viejas de Pytorch corriendo el siguiente comando en una consola:

***pip uninstall torch***

Seguidamente se debe instalar la versión 12.1 de CUDA mediante el siguiente [enlace](https://developer.nvidia.com/cuda-12-1-0-download-archive). (Descargue el archivo correspondiente y siga las instrucciones del instalador).

Después de instalar la versión 12.1 de CUDA reinicie el sistema y luego de reiniciar corra el siguiente comando en una consola:

***pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 --index-url https://download.pytorch.org/whl/cu121***

Este comando descargará e instalará varios archivos de tamaño considerable por lo que puede tomar algunos minutos en completarse (Se requiere una conexión a internet para ejecutar el comando de manera exitosa).

Una vez se ejecutó el comando anterior, reinicie nuevamente y, en una consola ejecute los siguientes comandos ***uno a uno***:
- python
- import torch
- torch.cuda.is_available()
  
Al ejecutar el comando "torch.cuda.is_available()" en la consola debería verse el mensaje "True". Si este es el caso puede ejecutar el programa de detección de placas normalmente.

Si no se recibe el mensaje "True", existe la posibilidad de que la GPU utilizada no tenga soporte para CUDA. Para verificar esto en una consola ejecute los siguientes comandos (sin el guión inicial) ***uno a uno***:
- python
- import torch
- torch.zeros(1).cuda()

Si se recibe el siguiente mensaje:

"Found GPU0 XXXXX which is of cuda capability #.#.
PyTorch no longer supports this GPU because it is too old."

La tarjeta gráfica utilizada ya no tiene soporte y no puede ser utilizada para correr la detección de placas en tiempo real. Es posible verificar las versiones de CUDA disponibles para cada generación de tarjetas gráficas en el siguiente [enlace](https://en.wikipedia.org/wiki/CUDA#GPUs_supported).

[Referencia:](https://stackoverflow.com/questions/60987997/why-torch-cuda-is-available-returns-false-even-after-installing-pytorch-with)

Meter el error de pip install
