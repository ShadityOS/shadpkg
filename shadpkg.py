import sys
from libs.installfile import installfile


args = sys.argv
del args[0]

if sys.platform == 'linux':
    try:
        if args[0] == "install":
            installfile(args[1])
    except IndexError:
        print("Please pass through some arguments")
else:
    print("Sorry, at the moment ShadPKG only works on linux")
