import os
import sys
import subprocess


def _is_package_installed(package_name):
    try:
        __import__(package_name)
        return True
    except ImportError:
        try:
            __import__(package_name.lower())
            return True
        except:
            try:
                result = subprocess.run([sys.executable, '-m','pip', 'show', '--quiet', package_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                return True
            except subprocess.CalledProcessError:
                return False

def _run_command(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"{e.stderr.strip()}")
        # pass

def install(package_name):
    if not _is_package_installed("colorama"):
        _run_command([sys.executable, '-m', 'pip', 'install', '--upgrade', 'colorama'])

    from colorama import Fore, Style
    if _is_package_installed(package_name) != True:
        print(f"{Fore.BLACK}[AIP]{Style.RESET_ALL} {package_name} installing ")
        if _run_command([sys.executable, '-m', 'pip', 'install', '--upgrade', package_name]) == None:
            print(f"{Fore.RED}[AIP]{Style.RESET_ALL} {package_name} not installed")
            exit()
        else:
            print(f"{Fore.GREEN}[AIP]{Style.RESET_ALL} {package_name} installed")


     


              
def __custom_exception_handler(exception_type, exception, traceback):
    if exception_type == ModuleNotFoundError:
        package_name = exception.name 
        install(package_name)
        os.execv(sys.executable, [sys.executable] + sys.argv)
    else:
        sys.__excepthook__(exception_type, exception, traceback)


sys.excepthook = __custom_exception_handler

