from utils.system import entornoGrafico, displayManager, appsAInstalar
from utils.system import ejecutarUnComando
from utils.files import copiarYPegarArchivo, copiarYPegarCarpeta, copiarYPegarArchivoSUDO, copiarYPegarCarpetaSUDO
#from utils.network import clonar_repo

def main():
    print("Iniciando DotInstall...\n")
    entornoGrafico()
    displayManager()
    appsAInstalar()

    copiarYPegarArchivo("~/.dot/.xprofile", "~") # Archivo .xprofile
    
    # Creación carpeta .config
    ejecutarUnComando("mkdir ~/.config")
    # Creación carpeta Screenshots (útil para Scrot)
    ejecutarUnComando("mkdir ~/Screenshots")
    # Copiar/Pegar carpeta Backgrounds
    copiarYPegarCarpeta("~/.dot/Backgrounds", "~/")
    
    # INICIO bspwm, sxhkd
    # Copiar/Pegar carpetas de bspwm, sxhkd en ~/.config del equipo
    copiarYPegarCarpeta("~/.dot/.config/bspwm", "~/.config/")
    copiarYPegarCarpeta("~/.dot/.config/sxhkd", "~/.config/")

    # Darle permisos de ejecución al archivo de bspwm (bspwmrc)
    ejecutarUnComando("chmod +x ~/.config/bspwm/bspwmrc")
    # FIN bspwm, sxhkd

    # INICIO Establecer distribución de teclado
    # Copiar/Pegar archivo de establecimiento distribución de teclado permanente
    copiarYPegarArchivoSUDO("~/.dot/00-keyboard.conf", "/etc/X11/xorg.conf.d/")
    # INICIO Establecer distribución de teclado

    # INICIO Laptop
    # Copiar/Pegar archivo de panel tactil laptop configuración
    equipo = input("¿Este equipo es una Laptop/Portatil?: (y/n)")
    if (equipo == "y"):
        copiarYPegarArchivoSUDO("~/.dot/40-libinput.conf", "/etc/X11/xorg.conf.d/")
        print("Panel tactil configurado correctamente")
    elif (equipo == "n"):
        print("Ok")
    else:
        print("Ok")

    # FIN Laptop

    # INICIO Instalar NVM
    curlDeNVM = "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash"
    ejecutarUnComando(curlDeNVM)
    input(f"Asegurate constantemente de que el curlDeNVM={curlDeNVM} este actualizado, lo puedes actualizar cambiando su valor por el más actual en la variable curlDeNVM " ["[ENTER]: "])
    # Copiar/Pegar archivo .bashrc
    copiarYPegarArchivo("~/.dot/.bashrc", "~/")
    # Ejecutar comando para aplicar cambios del .bashrc
    ejecutarUnComando("source ~/.bashrc")
    guiaInstalarNodeNpmConNVM = input("¿Deseas revisar una rápida guia sobre como instalar NodeJs/Npm con NVM? (y/n): ")
    if (guiaInstalarNodeNpmConNVM == "y"):
        print("1. nvm ls-remote (listar versiones de nodejs disponibles)\n2. nvm install v<version> (instalar la versión deseada reemplazando <version> con el número de la versión)\n3. nvm use <version> (Activar la versión de nodejs instalada)")
    elif (guiaInstalarNodeNpmConNVM == "n"):
        print("Ok")
    else:
        print("Ok")

    # FIN Instalar NVM

    # INICIO Polybar
    # Copiar/Pegar carpeta de polybar
    copiarYPegarCarpeta("~/.dot/.config/polybar", "~/.config/")
    # Darle permisos al archivo de launch.sh para polybar
    ejecutarUnComando("chmod +x ~/.config/polybar/launch.sh")
    # FIN Polybar

    # INICIO Montar/Desmontar Dispositivos USB (dotusb)
    # Darle permisos al archivo de ejecución script
    ejecutarUnComando("chmod +x ~/.dot/dotusb")
    # Copiar/Pegar archivo ejecutable en directorio /usr/local/bin para que sea un comando del sistema
    copiarYPegarArchivoSUDO("~/.dot/dotusb", "/usr/local/bin")
    print("Puedes usar el comando dotusb mount/unmount en terminal para montar y desmontar Pendrives USB")
    # FIN Montar/Desmontar Dispositivos USB (dotusb)

    # INICIO Rofi
    # Crear directorio de rofi themes
    ejecutarUnComando("mkdir -p ~/.local/share/rofi")
    ejecutarUnComando("mkdir -p ~/.local/share/rofi/themes/")
    #
    copiarYPegarArchivo("~/.dot/REPOS/ROFITHEMES/themes/windows11-list-light.rasi", "~/.local/share/rofi/themes/")
    # FIN Rofi

    # INICIO Kitty
    copiarYPegarCarpeta("~/.dot/.config/kitty", "~/.config/")
    # FIN Kitty

    # INICIO FastFetch
    copiarYPegarCarpeta("~/.dot/.config/fastfetch", "~/.config/")
    # FIN FastFetch



if __name__ == "__main__":
    main()
