#!C:\Users\ysc_c\PycharmProjects\seleniumwebinar\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'em==0.4.0','console_scripts','em'
__requires__ = 'em==0.4.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('em==0.4.0', 'console_scripts', 'em')()
    )
