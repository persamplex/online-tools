import os
import sys
import subprocess
import shutil
class AIP():
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
                    return result.returncode == 0 
                except subprocess.CalledProcessError:
                    return False

    def _run_command(command):
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"{e.stderr.strip()}")
            exit()

    def install(package_name):
        if not self._is_package_installed("colorama"):
            self._run_command([sys.executable, '-m', 'pip', 'install', '--upgrade', 'colorama'])
        from colorama import Fore, Style
        if self._is_package_installed(package_name):
            print(f"{Fore.BLACK}[AIP]{Style.RESET_ALL}{package_name} is already installed")
            pass
        else:
            print(f"{Fore.BLACK}[AIP]{Style.RESET_ALL} {package_name} installing ")
            if self._run_command([sys.executable, '-m', 'pip', 'install', '--upgrade', package_name]) == None:
                print(f"{Fore.RED}[AIP]{Style.RESET_ALL} {package_name} not installed")
                exit()
            else:
                print(f"{Fore.GREEN}[AIP]{Style.RESET_ALL} {package_name} installed")