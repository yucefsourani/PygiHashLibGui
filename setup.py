#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from distutils.core import setup
from glob import glob


doc_files  = ['LICENSE',  'README.md']
data_files = [
              ('share/applications/', ['com.github.yucefsourani.PygiHashLibGui.desktop']),
              ('share/doc/pygihashlibgui', doc_files),
              ('share/icons/hicolor/16x16/apps/', ['hicolor/16x16/apps/com.github.yucefsourani.PygiHashLibGui.png']),
              ('share/icons/hicolor/22x22/apps/', ['hicolor/22x22/apps/com.github.yucefsourani.PygiHashLibGui.png']),
              ('share/icons/hicolor/24x24/apps/', ['hicolor/24x24/apps/com.github.yucefsourani.PygiHashLibGui.png']),
              ('share/icons/hicolor/32x32/apps/', ['hicolor/32x32/apps/com.github.yucefsourani.PygiHashLibGui.png']),
              ('share/icons/hicolor/36x36/apps/', ['hicolor/36x36/apps/com.github.yucefsourani.PygiHashLibGui.png']),
              ('share/icons/hicolor/48x48/apps/', ['hicolor/48x48/apps/com.github.yucefsourani.PygiHashLibGui.png']),
              ('share/icons/hicolor/64x64/apps/', ['hicolor/64x64/apps/com.github.yucefsourani.PygiHashLibGui.png']),
              ('share/icons/hicolor/72x72/apps/', ['hicolor/72x72/apps/com.github.yucefsourani.PygiHashLibGui.png']),
              ('share/icons/hicolor/96x96/apps/', ['hicolor/96x96/apps/com.github.yucefsourani.PygiHashLibGui.png']),
              ('share/icons/hicolor/128x128/apps/',['hicolor/128x128/apps/com.github.yucefsourani.PygiHashLibGui.png']),
              ('share/pixmaps/',['hicolor/128x128/apps/com.github.yucefsourani.PygiHashLibGui.png']),
              ]

setup(
      name="PygiHashLibGui",
      description='Gui For hashLib',
      long_description='Gui For hashLib.',
      version="0.1",
      author='Youcef Sourani',
      author_email='youssef.m.sourani@gmail.com',
      url="https://github.com/yucefsourani/PygiHashLibGui",
      license='GPLv3 License',
      platforms='Linux',
      scripts=['pygihashlibgui'],
      keywords=['hash', 'hashlib'],
      classifiers=[
          'Programming Language :: Python',
          'Operating System :: POSIX :: Linux',
          'Development Status :: 4 - Beta ',
          'Intended Audience :: End Users/Desktop',
            ],
      data_files=data_files
)
