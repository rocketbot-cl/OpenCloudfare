# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
   sudo pip install <package> -t .

"""

import sys
import os

base_path = tmp_global_obj["basepath"] # type: ignore
cur_path = os.path.join(base_path, 'modules', 'OpenCloudfare', 'libs')

if cur_path not in sys.path:
    sys.path.append(cur_path)
    
try:
    from r_seleniumbase import Driver # type: 
    import r_seleniumbase.config as sb_config
    from r_selenium.webdriver.common.by import By
    from r_selenium.webdriver.support.ui import WebDriverWait
    from r_selenium.webdriver.support import expected_conditions as EC
    import r_seleniumbase.core.browser_launcher as launcher
    from time import sleep
except Exception as e:
    import traceback
    traceback.print_exc()
    raise e

GetGlobals = GetGlobals # type: ignore
GetParams = GetParams # type: ignore
SetVar = SetVar # type: ignore
PrintException = PrintException # type: ignore

web = GetGlobals('web')
module = GetParams("module")
global mod_cloudfare
global session

session = GetParams("session")
if not session:
    session = 'default'


if module == "open_browser":
    url_ = GetParams("url")
    session = GetParams("session")
    r= int(GetParams("retries") if GetParams("retries") else 1)
    var_ = GetParams("var")

    try:        
        import r_selenium as _sel
        import r_seleniumbase as _sb

        print(
            f"[diag] selenium={getattr(_sel, '__version__', 'unknown')} "
            f"({getattr(_sel, '__file__', 'unknown')}) | "
            f"seleniumbase={getattr(_sb, '__version__', 'unknown')} "
            f"({getattr(_sb, '__file__', 'unknown')})"
        )
        mod_cloudfare = Driver(uc=True)
        mod_cloudfare.maximize_window()
        sleep(1)
        mod_cloudfare.uc_open_with_reconnect(url_, r)
        web.driver_list[session] = mod_cloudfare
        web.driver_actual_id = session
        
        SetVar(var_, True)
    except Exception as e:
        PrintException()
        SetVar(var_, False)
        raise e

if module == "solve_captcha":
    session = GetParams("session")
    var_ = GetParams("var")

    try:
        driver = web.driver_list[session]
        print("Looking Captcha . . .")
        sleep(1.5)
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "iframe"))
            )
        except:
            pass
        driver.uc_gui_click_captcha()
        SetVar(var_, True)
        print("Captcha solved")
    except Exception as e:
        PrintException()
        print("The Captcha could not be solved.")
        SetVar(var_, False)

if module == "close_browser":
    session = GetParams("session")
    var_ = GetParams("var")

    try:
        if session in web.driver_list:
            driver = web.driver_list[session]
            driver.quit()
            del web.driver_list[session]
            SetVar(var_, True)
        else:
            print(f"Session '{session}' not found.")
            SetVar(var_, False)
    except Exception as e:
        PrintException()
        SetVar(var_, False)
        raise e