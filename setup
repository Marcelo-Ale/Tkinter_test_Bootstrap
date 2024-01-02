from sys import platform
from cx_Freeze import setup, Executable

base = None
if platform == 'win32':
    base = 'Win32Gui'

setup(
    name='Google_Translate',
    version='1.0',
    description='Tradutor feito na live de Python',
    options={
        'build_exe': {
            'includes': ['tkinter', 'ttkbootstrap']
        }
    },
