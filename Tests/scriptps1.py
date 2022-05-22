import subprocess, sys

getpcinfo = subprocess.Popen(["powershell.exe",
              "C:\\Users\\sabri\\PycharmProjects\\Agent\\data\\Get-ComputerInfo.ps1"],
              stdout=sys.stdout)
getpcinfo.communicate()