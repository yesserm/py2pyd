import sys
import os
import glob
import shutil

sys.path.insert(
    0, os.path.join(os.path.abspath(os.getcwd()), os.path.normpath("modules/py2pyd/libs"))
)
import distutils.cygwinccompiler

def patched_get_msvcr():
    return []

distutils.cygwinccompiler.get_msvcr = patched_get_msvcr

from Cython.Build import cythonize 
from setuptools import setup, Extension
ruta = os.environ.get("ruta_bot")


mingw_path = os.path.abspath("modules/py2pyd/libs/mingw/bin")
os.environ["PATH"] = mingw_path + os.pathsep + os.environ["PATH"]

if not os.path.exists(ruta):
    print("No se encontro la carpeta del bot")
else:
    for file in glob.glob(os.path.join(ruta, "*.pyd")):
        os.remove(file)
    ficheros = [os.path.join(ruta, f) for f in os.listdir(ruta) if f.endswith(".py") and f != "__init__.py"]
    name_ficheros = [f for f in os.listdir(ruta) if f.endswith(".py") and f != "__init__.py"]
    name_ficheros = [fichero.rstrip('.py') for fichero in name_ficheros]


    if len(name_ficheros) > 0:

        os.chdir(ruta)
        ext_modules = []
        for mod_name, fichero in zip( name_ficheros, ficheros):
            ext_modules.append(
                Extension(
                    mod_name,
                    [fichero],
                    libraries=["vcruntime140"],
                    library_dirs=["C:\\DentalRobot\\App3.0\\modules\\py2pyd\\libs\\python"],
                    extra_compile_args=["-Wno-div-by-zero", "-DMS_WIN32"],
                )
            )
        
        setup(
            name="BotModules",
            ext_modules=cythonize(ext_modules, compiler_directives={'language_level': "3"}),
        )
        
        for file in glob.glob(os.path.join(ruta, "*.c")):
            os.remove(file)
        for file in glob.glob(os.path.join(ruta, "*.o")):
            os.remove(file)
        for file in glob.glob(os.path.join(ruta, "*.def")):
            os.remove(file)
        #shutil.rmtree(ruta + r"\build")

        name_ficheros_pyd = [f for f in os.listdir(ruta) if f.endswith(".pyd")]
        for i, fichero in enumerate(name_ficheros):
            if fichero in name_ficheros_pyd[i]:
                os.rename( name_ficheros_pyd[i], fichero + ".pyd")

