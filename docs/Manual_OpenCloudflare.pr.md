



# OpenCloudflare

Módulo para abrir o Google Chrome e resolver o captcha Cloudflare Turnstile.

*Read this in other languages: [English](Manual_OpenCloudflare.md), [Português](Manual_OpenCloudflare.pr.md), [Español](Manual_OpenCloudflare.es.md)*

![banner](imgs/Banner_OpenCloudflare.jpg)
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
|Retries|Define quantas vezes o driver tentará recarregar a URL se o primeiro carregamento falhar.|5|
|Pasta de Downloads|Caminho para a pasta onde os downloads serão salvos.|C:/Users/User/Downloads|
|Altura|Altura da janela do navegador em pixels. Será usado se ocorrer um erro ao maximizar a janela.|1080|
|Largura|Largura da janela do navegador em pixels. Será usado se ocorrer um erro ao maximizar a janela.|1920|
|Auto baixar PDF|Baixa automaticamente arquivos PDF em vez de abri-los no navegador.||
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
