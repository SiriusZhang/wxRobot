# -*- coding: utf-8 -*-
import os

DB_NAME = 'wxRobot'

FILE_STORAGE_ROOT = ''

if os.name == 'nt': 
    FILE_STORAGE_ROOT = 'D:/wxRobot'
else:
    FILE_STORAGE_ROOT = '/data'