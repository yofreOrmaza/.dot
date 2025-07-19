import subprocess
import shlex

def activarServicio(servicio):
    nombreServicio = f"{servicio}.service"
    subprocess.run(["sudo", "systemctl", "enable", nombreServicio])

def ejecutarUnComando(comando):
    subprocess.run(shlex.split(comando))

def entornoGrafico():
    paquetes = ["xorg-server", "xorg-apps", "xorg-xinit"]
    subprocess.run(["sudo", "pacman", "-S", "--noconfirm"] + paquetes)

    driversUser = int(input("¿Qué drivers deseas instalar?\n1. Intel\n2. AMD\n3. Nvidia\n=> "))
    if (driversUser == 1):
        driver = ["xf86-video-intel"]
        subprocess.run(["sudo", "pacman", "-S", "--noconfirm"] + driver)
        driverAdicional = input("¿Deseas instalar un driver adicional? (y/n): ")
        if (driverAdicional == "y"):
            entornoGrafico()
        elif (driverAdicional == "n"):
            print("Ok")
            pass
        else:
            print("Ok")
    elif (driversUser == 2):
        driver = ["xf86-video-amdgpu"]
        subprocess.run(["sudo", "pacman", "-S", "--noconfirm"] + driver)
        driverAdicional = input("¿Deseas instalar un driver adicional? (y/n): ")
        if (driverAdicional == "y"):
            entornoGrafico()
        elif (driverAdicional == "n"):
            print("Ok")
            pass
        else:
            print("Ok")
    elif (driversUser == 3):
        driver = ["xf86-video-nouveau"]
        subprocess.run(["sudo", "pacman", "-S", "--noconfirm"] + driver)
        driverAdicional = input("¿Deseas instalar un driver adicional? (y/n): ")
        if (driverAdicional == "y"):
            entornoGrafico()
        elif (driverAdicional == "n"):
            print("Ok")
            pass
        else:
            print("Ok")
    else:
        print("Ingresa un valor de instalación válido")
        entornoGrafico()

    paquetes2 = ["bspwm", "sxhkd", "kscreen"]
    subprocess.run(["sudo", "pacman", "-S", "--noconfirm"] + paquetes2)


def displayManager():
    paquetes = ["ly"]
    subprocess.run(["sudo", "pacman", "-S", "--noconfirm"] + paquetes)

    activarServicio("ly")
    print("You can find all the configuration in /etc/ly/config.ini")


def appsAInstalar():
    paquetes = ["ttf-jetbrains-mono-nerd", "bash", "dmenu", "nitrogen", "fastfetch", "kitty", "xfce4", "arandr", "polybar", "git", "brightnessctl", "pcmanfm", "firefox", "openssh", "unzip", "udisks2", "scrot", "kolourpaint", "pipewire", "pulseaudio", "pavucontrol", "xdg-user-dirs", "btop", "libinput", "mpv", "okular", "flatpak", "rofi", "bluez", "bluez-utils", "blueman"]
    subprocess.run(["sudo", "pacman", "-S", "--noconfirm"] + paquetes)

    subprocess.run(["xdg-user-dirs-update"], cwd="/") # como ya se instalo xdg-user-dirs, pues este comando funciona para que el programa hago su tarea que es crea los directorios base del sistema
