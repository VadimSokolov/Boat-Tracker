from distutils.core import setup
import py2exe
options = {
    'py2exe': 
    {'dll_excludes': ['MSVCP90.dll','MSVCR80.dll'], "includes" : ["sip", "PyQt4", "PyQt4.QtNetwork", "PyQt4.QtXml"]}
    }

setup(console=['BoatTracker.py'], options=options)