



# OpenCloudflare

Módulo para abrir Google Chrome y resolver el captcha Cloudflare Turnstile.

*Read this in other languages: [English](Manual_OpenCloudflare.md), [Português](Manual_OpenCloudflare.pr.md), [Español](Manual_OpenCloudflare.es.md)*

![banner](imgs/Banner_OpenCloudflare.jpg)
## Como instalar este módulo

Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.


## Descripción de los comandos

### Abrir Navegador

Abre el navegador Chrome.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL|Direccion a la cual se desea acceder.|https://rocketbot.com/es|
|Retries|Define cuántas veces el driver intentará recargar la URL si la primera carga falla.|5|
|Carpeta de Descargas|Ruta hacia la carpeta donde se guardarán las descargas.|C:/Users/User/Downloads|
|Alto|Altura de la ventana del navegador en píxeles. Será usado si ocurre un error al maximizar la ventana.|1080|
|Ancho|Ancho de la ventana del navegador en píxeles. Será usado si ocurre un error al maximizar la ventana.|1920|
|Auto descargar PDF|Descarga automáticamente archivos PDF en lugar de abrirlos en el navegador.||
|Session|Identificador de sesión|1|
|Variable||res|

### Resolver Captcha Cloudflare

Resuelve el captcha Cloudflare que se encuentre presente en el navegador abierto.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Session|Identificador de sesión|1|
|Variable||res|

### Cerrar Navegador

Cierra una sesion de Chrome abierta por este módulo.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Session|Identificador de sesión|1|
|Variable||res|
