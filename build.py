#!/usr/bin/env python3

import sys
import os

if not os.path.isdir('build'):
    os.mkdir('build')

if not os.path.isdir('presentations') or \
   not os.path.isdir('publications') or \
   not os.path.isdir('data'):
    print("I can't find some key directories, are you sure you're running this in the right spot?")
    sys.exit(1)

os.system('markdown2 index.md > build/index.html')
os.system('cp -r presentations build/')
os.system('cp -r publications build/')
os.system('cp -r data build/')

os.system('markdown2 index.md > docs/index.html')
os.system('cp -r presentations docs/')
os.system('cp -r publications docs/')
os.system('cp -r data docs/')
