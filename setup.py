import sys
import py2exe
from distutils.core import setup
import shutil

sys.argv.append('py2exe')

setup(
    options={
        'py2exe': {'bundle_files': 1, 'compressed': True,
                   "includes":["os", "zipfile"]}
    },
    console=[
        {'script': "a.py"}
    ],
    zipfile=None,
)

shutil.move('dist\\a.exe', '.\\a.exe')
shutil.rmtree('build')
shutil.rmtree('dist')
