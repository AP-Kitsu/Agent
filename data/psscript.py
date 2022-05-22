# -*- coding: iso-8859-1 -*-
import subprocess, sys

def powershell():
    dataps = subprocess.Popen(["powershell.exe",
              "C:\\Users\\Kitsu\\PycharmProjects\\Agent\\data\\Get-ComputerInfo.ps1"],
              stdout=sys.stdout)
    return dataps
powershell().stdout
a = powershell().stdout
b = powershell().stderr
print(a)

if a is None: # se il numero è negativo
    print('Script avvenuto correttamente', a)
else:
    print('Script non avvenuto correttamente', b)


