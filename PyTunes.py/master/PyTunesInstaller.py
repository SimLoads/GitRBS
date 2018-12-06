##pytunes installer 0.6##
import time 
import os 
import urllib.request
def installer():
    os.system("cls")
    print("Welcome to the PyTunes installer!")
    print("1} Install PyTunes Now")
    print("2} Update PyTunes")
    print("3} Uninstall PyTunes")
    print("4} Exit")
    install = input("")
    print("")
    if install == ("1"):
        if not os.path.exists("PyTunes.py"):
            print("Downloading PyTunes...")
            update = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/PyTunes.py/master/PyTunes.py') 
            response = urllib.request.urlopen(update) 
            newcode = response.read() 
            master = newcode.decode()
            soundef1 = ('https://raw.githubusercontent.com/SimLoads/PyTunes.py/master/StartSnd.ogg')
            soundef2 = ('https://raw.githubusercontent.com/SimLoads/PyTunes.py/master/err.ogg')
            with open('installcode.pyd', 'w') as u: 
                u.write(master) 
                u.close 
            print('Installing...') 
            with open('installcode.pyd', 'r') as u: 
               with open('PyTunes.py', 'w', encoding='utf-8', newline='') as p: 
                   p.write(master)
                   urllib.request.urlretrieve(soundef1, 'StartSnd.ogg')
                   urllib.request.urlretrieve(soundef2, 'err.ogg')
                   os.system("attrib +s +h err.ogg")
                   os.system("attrib +s +h StartSnd.ogg")
                   p.close() 
                   u.close() 
                   os.remove('installcode.pyd') 
            print('Installed! Now starting...') 
            time.sleep(2) 
            os.startfile('PyTunes.py') 
            exit()
        else:
            print("PyTunes is already installed!")
            os.system("pause")
            installer()
    if install == ("2"):
        if os.path.exists("PyTunes.py"):
            print("Starting update manager...")
            if os.path.exists("updatemanager.py"):
                os.startfile("updatemanager.py")
                exit()
            else:
                os.system("echo import time >> updatemanager.py")
                os.system("echo import os >> updatemanager.py")
                os.system("echo import urllib.request >> updatemanager.py")
                os.system("echo os.system('title PyTunes Update Manager') >> updatemanager.py")
                os.system("echo print('Collecting update from github...') >> updatemanager.py")
                os.system("echo update = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/PyTunes.py/master/PyTunes.py') >> updatemanager.py")
                os.system("echo response = urllib.request.urlopen(update) >> updatemanager.py")
                os.system("echo newcode = response.read() >> updatemanager.py")
                os.system("echo master = newcode.decode() >> updatemanager.py")
                os.system("echo with open('update.pyd', 'w') as u: >> updatemanager.py")
                os.system("echo     u.write(master) >> updatemanager.py")
                os.system("echo     u.close >> updatemanager.py")
                os.system("echo print('Updating...') >> updatemanager.py")
                os.system("echo time.sleep(2) >> updatemanager.py")
                os.system("echo os.remove('PyTunes.py') >> updatemanager.py")
                os.system("echo with open('update.pyd', 'r') as u: >> updatemanager.py")
                os.system("echo    with open('PyTunes.py', 'w', encoding='utf-8', newline='') as p: >> updatemanager.py")
                os.system("echo        p.write(master) >> updatemanager.py")
                os.system("echo        p.close() >> updatemanager.py")
                os.system("echo        u.close() >> updatemanager.py")
                os.system("echo        os.remove('update.pyd') >> updatemanager.py")
                os.system("echo print('Updated! Now restarting...') >> updatemanager.py")
                os.system("echo time.sleep(2) >> updatemanager.py")
                os.system("echo os.startfile('PyTunes.py') >> updatemanager.py")
                os.system("echo exit() >> updatemanager.py")
                os.startfile("updatemanager.py")
                exit()
        else:
            print("PyTunes is not installed! Please install PyTunes first.")
            os.system("pause")
            installer()
    if install == ("3"):
        if os.path.exists("PyTunes.py"):
            print("Are you sure? PyTunes will be deleted. [y/n]")
            dele = input("")
            if dele == ("y"):
                os.remove("PyTunes.py")
                if os.path.exists("err.ogg"):
                    os.remove("err.ogg")
                if os.path.exists("StartSnd.ogg"):
                    os.remove("StartSnd.ogg")
                print("Uninstalled")
                os.system("pause")
                installer()
        else:
            print("PyTunes is not installed! Please install PyTunes first.")
            os.system("pause")
            installer()
    if install == ("4"):
        exit()
    else:
        installer()
installer()
