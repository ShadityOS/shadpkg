from zipfile import ZipFile
import os


def installfile(filelocation):
    try:
        file = ZipFile(filelocation)
        file.extractall(os.getcwd())
        file.close()
        meta = open("meta.txt", "r")
        for i, line in enumerate(meta):
            if i == 0:
                pkg_name = line
            elif i == 1:
                pkg_version = line
            elif i == 3:
                pkg_author = line
            elif i == 4:
                pkg_system = line
        os.system("sudo chmod -R +x exec")
        os.system("sudo cp -a exec/. /usr/bin")
        os.system("sudo mkdir /usr/share/shadpkg/" + pkg_name)
        os.system("sudo cp -a libs/. /usr/share/shadpkg/" + pkg_name)
        os.system("sudo cp meta.txt /usr/share/shadpkg/" + pkg_name)
        os.system("sudo rm -r exec && sudo rm -r libs && sudo rm meta.txt")
    except FileNotFoundError:
        print("Sorry, that file either does not exist or isn't in your current directory")

