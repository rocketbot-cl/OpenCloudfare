



# OpenCloudfare
  
Módulo para abrir Google Chrome y resolver el captcha Cloudfare Turnstile.  

*Read this in other languages: [English](Manual_OpenCloudfare.md), [Português](Manual_OpenCloudfare.pr.md), [Español](Manual_OpenCloudfare.es.md)*
  
![banner](imgs/Banner_OpenCloudfare.jpg)
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
|Session|Identificador de sesión|1|
|Variable||res|

### Resolver Captcha Cloudfare
  
Resuelve el captcha Cloudfare que se encuentre presente en el navegador abierto.
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
