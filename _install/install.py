# importing subprocess module
import subprocess

# importing urllib.requests for internet checking functions
import urllib.request


# initializing host to gfg.
def connect(host='https://www.geeksforgeeks.org/'):
    # trying to open gfg
    try:
        urllib.request.urlopen(host)
        return True

    # trying to catch exception when internet is not ON.
    except:
        return False


def main(module_name):
    # updating pip to latest version
    subprocess.run('python -m pip install --upgrade pip')

    # commanding terminal to pip install
    p = subprocess.run('pip3 install ' + module_name)

    # internet off
    if (p.returncode == 1 and connect() == False):
        print("error!! occurred check\nInternet conection")

    # Every thing worked fine
    elif (p.returncode == 0):
        print("It worked", module_name, " is installed")

    # Name of module wrong
    elif (p.returncode == 1 and connect() == True):
        print("error!! occurred check\nName of module")


module_name = input("Enter the module name: ")
main(module_name)
