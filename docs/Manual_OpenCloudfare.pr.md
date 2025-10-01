



# OpenCloudfare
  
Módulo para abrir o Google Chrome e resolver o captcha Cloudfare Turnstile.  

*Read this in other languages: [English](Manual_OpenCloudfare.md), [Português](Manual_OpenCloudfare.pr.md), [Español](Manual_OpenCloudfare.es.md)*
  
![banner](imgs/BANNER_OPENCLOUDFARE.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Abrir Navegador
  
Abre o navegador Chrome
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL|URL para acessar.|https://rocketbot.com/pr|
|Retries|Retries|5|
|Session|Identificador de sessão|1|
|Variável||res|

### Resolva o Captcha do Cloudflare
  
Resolva o captcha do Cloudflare que está presente no navegador aberto.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Session|Identificador de sessão|1|
|Variável||res|

### Fechar navegador
  
Fecha uma sessão do Chrome aberta por este módulo.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Session|Identificador de sessão|1|
|Variável||res|
