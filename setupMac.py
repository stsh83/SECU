from setuptools import setup

#APP would be the name of the file your code is in.
APP = ['Main.py']
DATA_FILES = ['Logo.gif', 'Centen.png', 'RealDeA8.png', 'ColumnariaVect.png', 'MoVta.png']
#The Magic is in OPTIONS.
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'mo.icns',
    'plist': {
        'CFBundleName': 'SECU',
        'CFBundleDisplayName': 'SECU',
        'CFBundleGetInfoString': "Spanish Empire Conversion Utilities",
        'CFBundleIdentifier': "com.sergio.osx.secu",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': u"Copyright © 2019, Sergio Serrano, All Rights Reserved"
         }
    }

setup(
    app=APP,
    name='Spanish Empire Conversion Utils', #change to anything
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)