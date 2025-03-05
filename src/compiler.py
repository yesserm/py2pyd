import sys
import os
import glob
import shutil

sys.path.insert(
    0, os.path.join(os.path.abspath(os.getcwd()), os.path.normpath("modules/py2pyd/libs"))
)

from Cython.Build import cythonize 
from setuptools import setup
ruta = os.environ.get("ruta_bot")

if not os.path.exists(ruta):
    print("No se encontro la carpeta del bot")
else:
    ficheros = [os.path.join(ruta, f) for f in os.listdir(ruta) if f.endswith(".py")]
    name_ficheros = [f for f in os.listdir(ruta) if f.endswith(".py")]
    name_ficheros = [fichero.rstrip('.py') for fichero in name_ficheros]
    if len(name_ficheros) > 0:

        os.chdir(ruta)
        
        setup(
            ext_modules=cythonize(ficheros)
        )
        
        for file in glob.glob(os.path.join(ruta, "*.c")):
            os.remove(file)
        shutil.rmtree(ruta + r"\build")

        name_ficheros_pyd = [f for f in os.listdir(ruta) if f.endswith(".pyd")]
        for i, fichero in enumerate(name_ficheros):
            if fichero in name_ficheros_pyd[i]:
                os.rename( name_ficheros_pyd[i], fichero + ".pyd")