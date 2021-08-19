# ShadPKG
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) ![](https://img.shields.io/github/issues/shadownightx/shadpkg.svg) [![GitHub license](https://img.shields.io/github/license/shadownightx/shadpkg.svg)](https://github.com/shadownightx/shadpkg/blob/main/LICENSE) <br>
A simple package manager coded in python for installing basic packages on Linux.

## Installation
Go to the <a href="https://github.com/ShadowNightX/shadpkg/releases">releases page </a>and download the latest ShadPKG zip. Unzip the file that you downloaded and open the folder that you extracted, in terminal. Make sure you have Python installed and run:
```
sudo python3 setup.py
```
##### NOTE: It is required that you run it in python3 and with sudo or else the setup will fail. 
<br> Once the setup is complete you should be able to access it by running ``` shadpkg ``` in terminal.

## Creating a spkg
To create your own SPKG (ShadPackage), you must follow the structure SPKGs use:
```
my-app.zip/
├─ exec/
│  ├─ executable1
│  ├─ executable2
│  ├─ executable3
├─ libs/
│  ├─ script1.py
│  ├─ library1.cpp
│  ├─ script2.cpp
│  ├─ library2.py
├─ meta.txt
```
### Meta.txt
The metadata for your package is stored here. Your meta.txt must follow the according structure: (Make sure to replace the placeholders with the actual values for your package)
```
package-name
version
author
OS
```
##### NOTE: ShadPKG currently only supports Linux so OS must be Linux.

### Libraries
Your libraries can be anything you want. Simple scripts that you want to keep separate from you executables to full blown libraries. The best thing is that they can 
be any kind of file that you like. Your package can also use this space to save any data your package needs. The libs folder for you package once it is installed 
is: ``` /usr/share/shadpkg/package-name ``` Be sure that the package-name is the same as in your meta.txt. The meta.txt file is also copied to the libs folder for your package.

### Exec
All executables stored under this directory will be transfered to ``` /usr/bin ``` folder so you don't have it can be run from any folder.

### Install your SPKG
Once you are done, select the two folder and your meta.txt, right-click and click ```Compress...```. Specify a name and compress it as a zip. Right-click and rename it to have a .spkg extension instead of .zip. Once that's completed, open terminal in the folder you created your spkg and run the following command: (Be sure to replace packagename with your package's filename)
```
shadpkg install packagename.spkg
```
Then you should be able to run the files that you put in the ```exec``` in any directory you like!

##### ShadPKG was made by ShadowNightX
