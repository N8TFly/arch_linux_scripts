import subprocess as sp
import signal
import getpass
import sys

# 1. input the nvidia installation file
filename = input("Enter a filename: ").strip("'")

# 2. ask for users password and store it in p
try:
    p = getpass.getpass()
except Exception as error:
    print("error", error)
else:
    print('success!')

# NOTE: to install Nvidia you have to be outside an X session, go to tty (ALT + F3-F6)

# 3. make file executable
sp.call("chmod +x .", filename)

#4. install manually
sp.call("sudo ", filename)

# 5. go through the installation process and write 'ok' when done
def pause():
    inp = input("Press 'ok' to continue: ")

    try:
        inp == 'ok':
        return True
    except SyntaxError as error:
        sys.exit(str(error))

# 6. get current kernel version
kernel_version = sp.check_output("uname -r", shell=True).decode("utf-8").strip("\n")

# 7. manually deploy modules (nvidida installer failes to do this properly)
sp.call("sudo depmod ", kernel_version)

# OTHERS

# check if GPU is detected and what driver is used
lspci -k | grep -A 2 -E "(VGA|3D)"
# save display settings if they are good like this
nvidia-xconfig
# uncomment Wayland Enable to force the GUI to use X when booting
sudo nano /etc/gdm/custom.conf
# Nvidia installer creates a file to blacklist nouveau (prevent it from starting), check if correctly done
# if this file is not present, create it
sudo nano nvidia-installer-disable-nouve au.conf 
