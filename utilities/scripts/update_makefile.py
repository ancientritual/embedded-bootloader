import re
import os

def update_makefile(makefile_path, original_path, new_path):
    with open(makefile_path, 'r') as file:
        filedata = file.read()

    filedata = re.sub(re.escape(original_path), re.escape(new_path), filedata)

    with open(makefile_path, 'w') as file:
        file.write(filedata)

makefile_path = 'implementations/samd20-optiboot-custom/samd20-optiboot-custom/Debug/Makefile'
original_path = r'C:\Program Files (x86)\Atmel\Studio\7.0\toolchain\arm\arm-gnu-toolchain\bin'
new_path = r'C:\ProgramData\chocolatey\lib\gcc-arm-embedded\tools\bin'

update_makefile(makefile_path, original_path, new_path)
