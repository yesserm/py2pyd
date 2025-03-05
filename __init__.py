from json import load
from pathlib import Path
import os
import sys
import shutil


current_path = Path(os.getcwd()).resolve()
sys.path.append(os.path.join(current_path, 'modules', 'py2pyd'))





try:
    module = GetParams("module")

    if module == "py2pyd":
        bot_name = GetParams("inputBotName")
 
        ruta_bot_dir = os.path.join('C:\DentalRobot', 'parallel', 'bots', bot_name)  
        os.environ["ruta_bot"] = ruta_bot_dir
        os.system(f"{os.getcwd()}\modules\py2pyd\libs\python\python.exe modules/py2pyd/src/compiler.py build_ext --inplace --build-lib {ruta_bot_dir}")
        

except Exception as e:
    print(f"Error: {e}")
    raise e
