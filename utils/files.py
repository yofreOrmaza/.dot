import subprocess
from utils.system import ejecutarUnComando

def copiarYPegarArchivo(rutaDeArchivoOrigen, rutaDeArchivoDestino):
    ejecutarUnComando(f"cp -r {rutaDeArchivoOrigen} {rutaDeArchivoDestino}")

def copiarYPegarCarpeta(rutaDeCarpetaOrigen, rutaDeCarpetaDestino):
    ejecutarUnComando(f"cp -r {rutaDeCarpetaOrigen} {rutaDeCarpetaDestino}")

def copiarYPegarArchivoSUDO(rutaDeArchivoOrigen, rutaDeArchivoDestino):
    ejecutarUnComando(f"sudo cp -r {rutaDeArchivoOrigen} {rutaDeArchivoDestino}")

def copiarYPegarCarpetaSUDO(rutaDeCarpetaOrigen, rutaDeCarpetaDestino):
    ejecutarUnComando(f"sudo cp -r {rutaDeCarpetaOrigen} {rutaDeCarpetaDestino}")