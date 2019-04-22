# -*- mode: python -*-
#sudo pyinstaller Conv.spec

block_cipher = None


a = Analysis(['Main.py'],
             pathex=['C:\\Conversion'],
             binaries=[],
             datas=[('favicon.ico', '.'),
             ('Logo.gif', '.'),
             ('Centen.png', '.'),
             ('RealDeA8.png', '.'),
             ('ColumnariaVect.png', '.'),
             ('MoVta.png', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='SECU',
          debug=False,
          strip=False,
          upx=True,
          console=False)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='SECU')
