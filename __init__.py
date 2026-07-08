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
cur_path = os.path.join(base_path, 'modules', 'OpenCloudflare', 'libs')

if cur_path not in sys.path:
    sys.path.append(cur_path)
    
try:
    from r_seleniumbase import Driver # type: 
    import r_seleniumbase.config as sb_config
    from r_selenium.webdriver.common.by import By
    from r_selenium.webdriver.support.ui import WebDriverWait
    from r_selenium.webdriver.support import expected_conditions as EC
    import r_seleniumbase.core.browser_launcher as launcher
    from pathlib import Path
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


def is_a_maximize_error(error):
    error_text = str(error)
    return (
        '"code":-32000' in error_text
        and '"Browser window not found"' in error_text
    )


def get_by_selector(data_type):
    selector_map = {
        "xpath": By.XPATH,
        "css": By.CSS_SELECTOR,
        "id": By.ID,
        "name": By.NAME,
        "link_text": By.LINK_TEXT,
        "partial_link_text": By.PARTIAL_LINK_TEXT,
        "tag_name": By.TAG_NAME,
        "class_name": By.CLASS_NAME,
    }
    return selector_map.get((data_type or "xpath").strip().lower(), By.XPATH)


def get_wait_condition(condition, locator):
    condition_map = {
        "clickable": EC.element_to_be_clickable,
        "visible": EC.visibility_of_element_located,
        "not_visible": EC.invisibility_of_element_located,
        "present": EC.presence_of_element_located,
    }
    wait_condition = condition_map.get((condition or "clickable").strip().lower(), EC.element_to_be_clickable)
    return wait_condition(locator)


def get_driver_from_session(web_obj, session_param):
    session_key = session_param if session_param not in [None, ""] else None
    available_sessions = list(web_obj.driver_list.keys())

    if session_key is not None and session_key in web_obj.driver_list:
        return session_key, web_obj.driver_list[session_key]

    actual_session = getattr(web_obj, "driver_actual_id", None)
    if actual_session in web_obj.driver_list:
        return actual_session, web_obj.driver_list[actual_session]

    if "default" in web_obj.driver_list:
        return "default", web_obj.driver_list["default"]

    if None in web_obj.driver_list:
        return None, web_obj.driver_list[None]

    if "" in web_obj.driver_list:
        return "", web_obj.driver_list[""]

    raise Exception(f"No active browser session found. Available sessions: {available_sessions}")


if module == "open_browser":
    url_ = GetParams("url")
    session = GetParams("session") or "default"
    r= int(GetParams("retries") if GetParams("retries") else 1)
    var_ = GetParams("var")
    download_dir = GetParams("download_dir")
    height = GetParams("height") or "1080"
    width = GetParams("width") or "1920"
    auto_download_pdf = GetParams("auto_download_pdf") or False

    if isinstance(auto_download_pdf, str):
        auto_download_pdf = auto_download_pdf.strip().lower() in ["true", "1", "yes"]
    else:
        auto_download_pdf = bool(auto_download_pdf)

    try:
        from r_seleniumbase.core import download_helper

        if download_dir:
            download_helper.set_downloads_folder(download_dir)
        else:
            download_helper.set_downloads_folder(str(Path.home() / "Downloads"))
        
        mod_cloudfare = Driver(uc=True, external_pdf=auto_download_pdf)

        try:
            mod_cloudfare.maximize_window()
            sleep(1)
        except Exception as e:
            print("An error has occurred while trying to maximize the window")
            if is_a_maximize_error(e):
                try:
                    mod_cloudfare.set_window_size(int(width), int(height))
                    sleep(1)
                except Exception:
                    print("An error has occurred while trying to set the window's size")
            else:
                raise

        mod_cloudfare.uc_open_with_reconnect(url_, r)

        web.driver_list[session] = mod_cloudfare
        web.driver_actual_id = session
        
        SetVar(var_, True)
    except Exception as e:
        PrintException()
        SetVar(var_, False)
        raise e

if module == "solve_captcha":
    session = GetParams("session") or "default"
    var_ = GetParams("var")

    try:
        _, driver = get_driver_from_session(web, session)
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
    session = GetParams("session") or "default"
    var_ = GetParams("var")

    try:
        resolved_session, driver = get_driver_from_session(web, session)
        if resolved_session in web.driver_list:
            driver.quit()
            del web.driver_list[resolved_session]
            SetVar(var_, True)
        else:
            print(f"Session '{session}' not found.")
            SetVar(var_, False)
    except Exception as e:
        PrintException()
        SetVar(var_, False)
        raise e

if module == "wait_for_object":
    session = GetParams("session")
    data = GetParams("data")
    data_type = GetParams("data_type")
    wait_max = GetParams("wait_max")
    condition = GetParams("condition")
    result = GetParams("result")

    try:
        _, driver = get_driver_from_session(web, session)
        locator = (get_by_selector(data_type), data)
        max_wait = float(wait_max) if wait_max not in [None, ""] else 10.0
        founded = WebDriverWait(driver, max_wait).until(get_wait_condition(condition, locator))
        SetVar(result, bool(founded))
    except Exception as e:
        if e.__class__.__name__ != "TimeoutException":
            PrintException()
        SetVar(result, False)